# TEST_CASES.md

---

## Case 1：一般情況（正常輸入）— Task 1

**對應測試函式**：`tests/test_task1.py::TestTask1SequenceClean::test_dedupe_keep_order`

**輸入**：
```
5 3 5 2 9 2 8 3 1
```

**預期輸出**：
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**實際輸出**：
```
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```

**結果**：PASS

**失敗到通過的關鍵修改**：原本用 `set()` 去重導致順序不定，改用 `seen = set()` + `result = []` 手動追蹤順序後通過。

---

## Case 2：邊界情況（空輸入）— Task 3

**對應測試函式**：`tests/test_task3.py::TestTask3LogSummary::test_empty_logs`

**輸入**：
```
0
（無後續資料行）
```

**預期輸出**：
```
（無使用者列）
top_action: NONE 0
```

**實際輸出**：
```
top_action: NONE 0
```

**結果**：PASS

**失敗到通過的關鍵修改**：原本 `action_counts.most_common(1)[0]` 在空 Counter 時拋 `IndexError`，加入 `if action_counts` 判斷後改回傳 `("NONE", 0)` 才通過。

---

## Case 3：重複值與同分排序情況 — Task 2

**對應測試函式**：`tests/test_task2.py::TestTask2StudentRanking::test_ranking_tie_break`

**輸入**：
```
5 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
eva 92 20
```

**預期輸出**：
```
eva 92 20
zoe 92 21
bob 88 19
```

**實際輸出**：
```
eva 92 20
zoe 92 21
bob 88 19
```

**結果**：PASS

**失敗到通過的關鍵修改**：原本只用 `-score` 排序，同分學生順序不穩定，補上 `(age, name)` 為次要鍵後正確排出 bob 在 ian 之前（同分同齡時按名字升序）。

---

## Case 4：反例（容易寫錯）— Task 1 負數偶數

**對應測試函式**：`tests/test_task1.py::TestTask1SequenceClean::test_filter_evens_with_negatives`

**輸入**（直接呼叫函式）：
```python
filter_evens([7, -4, 0, 9, 2, 11])
```

**預期輸出**：
```python
[-4, 0, 2]
```

**實際輸出**：
```python
[-4, 0, 2]
```

**結果**：PASS

**失敗到通過的關鍵修改**：Python 的 `%` 對負數回傳負餘數（`-4 % 2 == 0`），判斷式 `x % 2 == 0` 本身正確，但若誤用 `x % 2 != 1` 就會漏掉 `0`，確認邏輯後無需修改。

---

## Case 5：最能測出錯誤的一組 — Task 3 使用者同總數時按名字排序

**對應測試函式**：`tests/test_task3.py::TestTask3LogSummary::test_summarize_logs_basic`

**輸入**：
```
6
alice login
bob login
alice view
bob view
chris login
chris view
```

**預期輸出**：
```
alice 2
bob 2
chris 2
top_action: login 3
```

**實際輸出**：
```
alice 2
bob 2
chris 2
top_action: login 3
```

**結果**：PASS

**失敗到通過的關鍵修改**：原本排序 key 只有 `-count`，三人同數時順序取決於 `defaultdict` 插入順序（不穩定），補上第二排序鍵 `x[0]`（使用者名稱升序）後，alice → bob → chris 才能穩定輸出。