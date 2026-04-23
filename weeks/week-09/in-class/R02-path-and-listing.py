# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path 物件可用 / 直接串接路徑，
# 比手動字串相加更直觀，也更不容易出錯。
# 同一份程式在不同作業系統會自動套用正確分隔符。
base = Path("weeks") / "week-09"
print(base)              # weeks/week-09（Windows 會自動變成反斜線）
print(base.name)         # week-09
print(base.parent)       # weeks
print(base.suffix)       # ''（無副檔名）

# 常見屬性說明：
# - name: 最後一節路徑名稱（檔名含副檔名）
# - parent: 上層資料夾
# - suffix: 副檔名（含 .）
# - stem: 檔名主體（不含副檔名）
f = Path("hello.txt")
print(f.stem, f.suffix)  # hello .txt

# 相容舊寫法：os.path.join
# 在舊程式碼裡仍很常見，功能是安全地組合路徑字串。
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
# 在開檔或建立流程前，先判斷 exists/is_file/is_dir 是好習慣，
# 可以避免路徑錯誤造成例外中斷。
p = Path("hello.txt")
print(p.exists())    # 是否存在
print(p.is_file())   # 是否是檔案
print(p.is_dir())    # 是否是資料夾

missing = Path("no_such_file.txt")
if not missing.exists():
    # 實務上可在這裡選擇建立預設檔案或直接跳過。
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")

# 只列當層
# os.listdir() 只回傳名稱（str），不含完整 Path 物件資訊。
for name in os.listdir(here):
    print("listdir:", name)

# 只抓 .py（當層）
# glob("*.py") 僅搜尋目前資料夾，不會進入子資料夾。
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓所有 .py（含子資料夾）
# rglob("*.py") = recursive glob，會一路往下搜尋。
# 若專案很大，結果可能很多；示範時可先 break 控制輸出量。
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用，只印第一個
