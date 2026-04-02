
# AI_USAGE.md

## 1. 我問了哪些問題（條列 3~5 條）

1. 「`dedupe` 保留第一次出現順序，為什麼不能直接用 `set()`？請解釋原理。」
2. 「Task 2 的多重排序 key 要怎麼設計？`(-score, age, name)` 的 tuple 排序優先順序是什麼？」
3. 「`defaultdict(int)` 和 `Counter` 在統計次數時有什麼差異，各自適合什麼場景？」
4. 「`unittest` 的 `TestCase.assertEqual` 和直接用 `assert` 有什麼不同？為什麼正式測試偏好 `unittest`？」
5. 「Task 3 空輸入 `m=0` 時，`Counter.most_common(1)` 會回傳什麼？要怎麼防範空序列的 IndexError？」

---

## 2. AI 給了哪些建議我有採用

- **函式拆分原則**：AI 建議將每個功能獨立成單一函式（`parse_input`、`dedupe_keep_order`、`sort_ascending` 等），方便測試與重用，我全部採納。
- **排序 key 的 tuple 技巧**：AI 說明用 `(-score, age, name)` 作為 key 可以同時表達「高分優先、同分按年齡升序、再按名字升序」，比多次 `sort()` 更效率，我採用此方式。
- **`Counter.most_common(1)` 的用法**：AI 解釋這是取頻率最高的一項的標準寫法，比手動排序 `.items()` 更簡潔，我在 Task 3 中採用。
- **`defaultdict(int)` 初始化無需判斷**：AI 提醒不用寫 `if user not in user_counts` 的判斷，直接 `user_counts[user] += 1` 就行，我採用。

---

## 3. AI 給了哪些建議我拒絕（以及原因）

- **AI 想直接幫我生成完整 `TEST_CASES.md`**：我拒絕，因為設計測資是作業要求學生自己思考的核心能力，若直接複製 AI 輸出就失去驗證自己理解程度的機會。
- **AI 建議用第三方套件 `pytest`**：它說 `pytest` 的語法更簡潔，但作業明確要求使用內建 `unittest`，且不需額外安裝套件，我仍使用 `unittest`。
- **AI 建議在 `main()` 中加入過多例外處理**：例如對非數字輸入加 `try/except ValueError`，但題目沒有這類需求，加入後反而掩蓋真正的輸入錯誤，我只保留邊界狀況的判斷（如 `m=0`）。

---

## 4. AI 可能誤導但我自行修正的案例

**案例：Task 2 的 `parse_student` 解析錯誤**

AI 最初建議的 `parse_student` 直接用 `line.split()` 後以索引取值，未說明若輸入行格式有誤（例如多餘空白或欄位順序錯誤）會在哪裡出問題。執行後出現 `ValueError: invalid literal for int() with base 10: 'python'`，原因是我在終端機測試時不小心把指令本身的字串貼入了輸入。

**修正**：我重新確認輸入格式必須嚴格為 `name score age` 三欄，並在測試案例中加入符合格式的輸入，驗證解析正確後才提交。這也讓我理解「測試時的輸入來源」和「程式邏輯本身」要分開排查。

