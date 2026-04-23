# U03. 文字 vs 位元組、編碼觀念（5.1 encoding / 5.4）
# Bloom: Understand — 能解釋什麼時候用 'rb'、為什麼要指定 encoding

from pathlib import Path

# ── 5.4 二進位讀寫：圖片、zip、任何非文字 ───────────────
# 這段重點：
# - 圖片、壓縮檔、音訊檔等屬於「二進位資料」，不是純文字。
# - 這類檔案要用 bytes 讀寫（rb / wb），而不是文字模式。
# - 很多檔案格式開頭有固定簽章（magic number），
#   PNG 的前 8 bytes 固定為 89 50 4E 47 0D 0A 1A 0A。
# 先造一個「假 PNG」：只寫入檔頭簽章，作為示範。
magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
Path("fake.png").write_bytes(magic)

# 讀回前 8 bytes，對照 PNG 檔頭
# open(..., "rb") 的 b 代表 binary，read() 回傳型別為 bytes。
with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)           # b'\x89PNG\r\n\x1a\n'
print(head == magic)  # True

# bytes 可逐位元組迭代（拿到 int，不是 str）
# 注意：
# - str 逐項迭代得到的是「字元」
# - bytes 逐項迭代得到的是 0~255 的整數
for b in head[:4]:
    print(b, hex(b))

# ── 文字 vs 位元組的型別差 ─────────────────────────────
s = "你好"
# encode/decode 是文字處理核心：
# - encode("utf-8"): str -> bytes（編碼）
# - decode("utf-8"): bytes -> str（解碼）
b = s.encode("utf-8")   # str → bytes
print(s, type(s))       # <class 'str'>
print(b, type(b))       # <class 'bytes'>
print(b.decode("utf-8"))  # bytes → str

# ── 5.1 encoding 參數：寫錯會爛掉 ──────────────────────
# 寫入文字檔時建議一律明示 encoding，
# 避免不同作業系統或環境的預設編碼不一致造成亂碼。
Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

# 正常：用 utf-8 讀 utf-8 寫的檔
print(Path("zh.txt").read_text(encoding="utf-8"))

# 故意弄錯：用 big5 解 utf-8 → UnicodeDecodeError
# 同一段 bytes 若用錯誤編碼解讀，常見結果是：
# 1) 直接丟 UnicodeDecodeError
# 2) 或讀出亂碼（視資料內容而定）
try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    # 教學示範：捕捉例外，讓程式不中斷並觀察錯誤訊息。
    print("解碼錯誤:", e)

# 小結：
# - 文字檔 → 'rt'/'wt'，一律明示 encoding='utf-8'
# - 非文字（png/zip/pickle）→ 'rb'/'wb'，不談 encoding
