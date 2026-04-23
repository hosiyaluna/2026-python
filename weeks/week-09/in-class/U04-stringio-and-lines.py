# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 提供「像檔案一樣」的介面（write/read/seek/iter），
# 但資料實際存放在記憶體，不會落到磁碟。
# 這就是常說的 duck typing（鴨子型別）：
# 「只要行為像檔案（有 read/write 等方法），就能當檔案用」。
# 適合：
# 1) 單元測試（避免建立暫存檔）
# 2) 暫時組裝文字內容再一次性取出
# 3) 要餵給只接受 file-like 參數的函式
buf = io.StringIO()
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串
# getvalue() 會回傳目前緩衝區的完整文字內容（str）。
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# 也能當讀檔用：seek 回開頭再逐行讀
# StringIO 內部也有「檔案指標」：
# - 前面寫入後，指標在尾端
# - 若要重新讀，需先 seek(0) 回到開頭
buf.seek(0)
for i, line in enumerate(buf, 1):
    # line 通常含結尾換行，rstrip() 可讓輸出更整齊
    print(i, line.rstrip())

# 為什麼有用？任何收 file-like 的 API（csv、json、logging）
# 都能塞 StringIO，不必真的寫到磁碟、方便測試。
import csv
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
# 直接取得 CSV 文字結果，不需建立 .csv 實體檔。
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先造一個多行檔
# Path.write_text() 可快速寫入整段文字到檔案。
# 這裡刻意放入空行，等等示範如何過濾。
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：過濾空行、加上行號、寫到新檔
dst = Path("poem_numbered.txt")
# 這裡在同一個 with 內同時開啟輸入與輸出檔：
# - fin: 讀取來源
# - fout: 寫入結果
# 不論中途是否發生例外，離開 with 區塊都會自動 close。
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    # n 用來記錄「非空行」的行號
    n = 0
    for line in fin:               # 逐行：一次只讀一行到記憶體
        # 去掉行尾空白與 \n，便於判斷是否空行。
        # 這裡使用 rstrip()，只處理右側；不影響行首縮排內容。
        line = line.rstrip()
        if not line:
            continue               # 跳過空行
        n += 1
        # :02d 代表至少兩位數，不足補 0（01, 02, ...）
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
# 讀出結果檔確認輸出內容
print(dst.read_text(encoding="utf-8"))
