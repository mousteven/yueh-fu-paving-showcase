# -*- coding: utf-8 -*-
# 公開版相簿資料:排除「報價與業務文件」資料夾,並把雲林肉品市場的真實合約金額/公司名稱改成教學用的模糊描述
import json
import sys
import importlib.util
from pathlib import Path

PRIVATE_SCRIPT = Path(r"C:\Users\User\Projects\岳父工程學徒\notes\build_gallery_data.py")
ROOT = Path(r"C:\Users\User\Projects\岳父工程學徒-公開版")
PHOTOS = ROOT / "photos"
OUT = ROOT / "gallery_data.js"

spec = importlib.util.spec_from_file_location("build_gallery_data", PRIVATE_SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules["build_gallery_data"] = mod
spec.loader.exec_module(mod)
meta = dict(mod.meta)

# 拿掉整個報價文件資料夾(相簿+facts都不放公開版)
meta.pop("15_報價與業務文件", None)

# 拿掉工地負責人的真實姓名(個人姓名,不是公司,不放公開版)
if "03_官田大內學甲公共工程" in meta:
    m03 = dict(meta["03_官田大內學甲公共工程"])
    m03["facts"] = [
        f.replace("監造永越景觀規劃設計、施工柏承營造有限公司,工地負責人沈漢庭", "監造永越景觀規劃設計、施工柏承營造有限公司")
        for f in m03["facts"]
    ]
    meta["03_官田大內學甲公共工程"] = m03

# 雲林肉品市場:拿掉真實合約總價與公司名稱配對,只留下「植草磚工程規模」這個教學重點
meta["13_雲林肉品市場"] = {
    "title": "雲林肉品市場",
    "confidence": "g",
    "desc": "雲林縣虎尾鎮的肉品市場整建工程,連鎖磚廣場、黑白相間安全島柱列、豬造型雕塑。",
    "facts": [
        "官方全名:雲林縣肉品市場整建工程(含112年建構肉品批發市場現代化屠宰及冷鏈設施設備計畫)",
        "地址:雲林縣虎尾鎮延平里下南100號",
        "業主:雲林縣肉品市場股份有限公司",
        "承造:中鴻營造有限公司",
        "設計監造:羿寬建築師事務所",
        "施工期限:112/12/29~115/09/15",
        "這是岳父參與過規模最大的植草磚工程之一,舖設面積超過千坪等級(實際分包金額與合約明細屬業務機密,未公開)",
    ],
}

data = []
for folder in sorted(PHOTOS.iterdir()):
    if not folder.is_dir():
        continue
    name = folder.name
    files = sorted(p.name for p in folder.iterdir() if p.suffix.lower() == ".jpg")
    m = meta.get(name, {"title": name, "confidence": "n", "desc": "", "facts": []})
    data.append({
        "folder": name,
        "title": m["title"],
        "confidence": m["confidence"],
        "desc": m["desc"],
        "facts": m["facts"],
        "count": len(files),
        "files": files,
    })

with open(OUT, "w", encoding="utf-8") as f:
    f.write("const GALLERY_DATA = ")
    json.dump(data, f, ensure_ascii=False, indent=0)
    f.write(";\n")

print(f"寫入 {OUT},共 {len(data)} 個資料夾,{sum(d['count'] for d in data)} 張照片")
