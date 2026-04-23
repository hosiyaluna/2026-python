# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入文字檔常見標準寫法：
# 1) mode='wt'：文字模式 + 覆寫寫入
#    - w: write，若檔案已存在會先清空
#    - t: text，文字模式（預設就是 t，但寫出來更清楚）
# 2) encoding='utf-8'：處理中文時建議明確指定，避免預設編碼差異
# 3) with open(...)：區塊結束自動關檔，避免資源未釋放
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    # write() 不會自動加換行，若要換行需自行加上 \n。
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回方式 A：一次讀完整份檔案（f.read()）
# 優點：寫法簡潔；缺點：大檔會吃較多記憶體。
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 一次讀完（小檔才適合）

# 讀回方式 B：逐行讀取（for line in f）
# 優點：記憶體友善，實務上讀大檔常用。
with open(path, "rt", encoding="utf-8") as f:
    for line in f:
        # line 通常含行尾 \n，使用 rstrip() 讓輸出更乾淨。
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print() 預設輸出到終端機。
# 指定 file=f 後，就能把 print 內容直接寫到檔案。
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # *fruits 會把串列元素拆成多個位置參數
    # sep="," 設定欄位分隔符
    # end="\n" 設定本次 print 的結尾（預設也是換行）
    print(*fruits, sep=",", end="\n", file=f)

# end='' 可避免這次 print 自動換行，
# 常用於要「同一行分段輸出」的情境。
with open("fruits.csv", "at", encoding="utf-8") as f:
    # a: append，追加寫入，不會覆蓋既有內容
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

# Path.read_text() 是快速讀文字檔的小工具。
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 核心觀念：
# - 文字模式（'rt'/'wt'）處理 str
# - 二進位模式（'rb'/'wb'）處理 bytes
# 若在文字模式寫 bytes，會觸發 TypeError。
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # ← 會錯
except TypeError as e:
    # 教學示範：捕捉錯誤，觀察錯誤訊息內容。
    print("錯誤示範:", e)
