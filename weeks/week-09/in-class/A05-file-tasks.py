# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
# date.today().isoformat() 會得到 YYYY-MM-DD 格式字串，
# 例如 2026-04-23，適合直接拿來當檔名的一部分。
today = date.today().isoformat()          # 例如 2026-04-23
diary = Path(f"diary-{today}.txt")

try:
    # mode='x'（exclusive create）重點：
    # - 檔案不存在：成功建立並寫入
    # - 檔案已存在：丟 FileExistsError
    # 這正好符合「每天只能建一次」的需求。
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 日記\n")
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 捕捉「檔案已存在」這個預期情況，
    # 並明確告知使用者不會覆蓋原內容。
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 走訪目錄 → 逐檔逐行讀 → 累計三個數字
def count_py(folder: Path):
    # total: 檔案總行數（包含空行）
    # nonblank: 非空白行（去頭尾空白後仍有內容）
    # defs: 以 def 開頭的函式宣告行
    total, nonblank, defs = 0, 0, 0

    # rglob('*.py') 會遞迴走訪 folder 與所有子資料夾中的 .py 檔。
    for p in folder.rglob("*.py"):
        # errors='replace' 可避免少數編碼異常檔案讓程式中斷。
        # 讀不到的字元會用替代符號表示，但統計流程可繼續。
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1

                # strip() 後的 s 用於空白判斷與關鍵字判斷。
                s = line.strip()
                if s:
                    nonblank += 1

                # 只計算「去空白後以 def 開頭」的行。
                # 範例："def foo():"、"    def bar(self):" 都會被算到。
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

# 示範目標資料夾：week-04/in-class
# 這裡用相對路徑，從目前檔案執行目錄往上兩層再進 week-04/in-class。
target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 若示範資料夾不存在，不拋錯，改用提示訊息收斂流程。
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
