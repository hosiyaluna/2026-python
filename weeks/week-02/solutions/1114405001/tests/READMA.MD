1114405001 楊能安
Week 02 作業提交  

完成題目清單
Task 1：Sequence Clean  
Task 2：Student Ranking  
Task 3：Log Summary  

執行方式
使用版本python3.14.3

程式執行指令

Task 1
```bash
python task1_sequence_clean.py

Task 2
python task2_student_ranking.py

Task 3
python task3_log_summary.py

測試執行指令
pytest tests/test_task1.py
pytest tests/test_task2.py
pytest tests/test_task3.py

Red → Green → Refactor 摘要

**Task 1：Sequence Clean**
- Red：先寫 `test_dedupe_keep_order`，直接呼叫尚不存在的 `dedupe_keep_order()`，測試立即報 `ImportError`，確認 Red 成立。
- Green：實作以 `seen = set()` 搭配 `result = []` 追蹤順序的去重邏輯，以及 `filter_evens` 的 list comprehension，測試全部通過。
- Refactor：將函式名稱從一開始較模糊的 `dedupe` 改為 `dedupe_keep_order`，明確表達「保留順序」的語意，並確認測試仍全綠。

**Task 2：Student Ranking**
- Red：先寫 `test_ranking_tie_break`，放入同分不同 age/name 的學生資料，驗證預期排名順序，此時 `rank_students` 尚未實作，測試報 `ImportError`。
- Green：用 `sorted(..., key=lambda s: (-s["score"], s["age"], s["name"]))` 一行完成三重排序，測試通過；另外在終端機測試手動輸入時，曾把指令本身誤貼入 stdin 導致 `ValueError`，確認後是操作失誤，程式邏輯本身正確。
- Refactor：拆出 `top_k_students` 函式負責切片前 k 名，避免 `main()` 過胖，並補充 k 超過學生數時直接回傳全部的邊界測試。

**Task 3：Log Summary**
- Red：先寫 `test_empty_logs`，傳入空 list，預期 `top_action` 回傳 `"NONE"` 而非 `None`，測試報 `AssertionError`，確認 Red 成立。
- Green：在 `summarize_logs` 中加入 `if action_counts` 的判斷，空輸入時回傳 `("NONE", 0)`，測試通過。
- Refactor：將使用者排序邏輯抽為獨立一行 `sorted(..., key=lambda x: (-x[1], x[0]))`，並加上關鍵字說明排序規則，閱讀性提升且測試仍全綠。