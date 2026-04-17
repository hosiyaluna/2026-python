# TEST_LOG.md

---

## 執行紀錄 1 — Red（測試尚未通過）

**執行指令**：
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**執行結果**：
```
ERROR: test_dedupe_keep_order (test_task1.TestTask1SequenceClean)
ImportError: cannot import name 'dedupe_keep_order' from 'task1_sequence_clean'

ERROR: test_ranking_tie_break (test_task2.TestTask2StudentRanking)
ImportError: cannot import name 'rank_students' from 'task2_student_ranking'

ERROR: test_empty_logs (test_task3.TestTask3LogSummary)
AssertionError: None != 'NONE'

----------------------------------------------------------------------
Ran 9 tests in 0.014s

FAILED (errors=2, failures=1)
```

**測試總數**：9　｜　**通過**：6　｜　**失敗/錯誤**：3

**修改說明**：
- Task 1 將函式 `dedupe` 改名為 `dedupe_keep_order`、`sort_asc` 改為 `sort_ascending`、`sort_desc` 改為 `sort_descending`，使名稱與測試 import 一致。
- Task 2 新增 `rank_students` 與 `top_k_students` 函式；Task 3 將空輸入時的回傳值從 `None` 改為 `"NONE"`。

---

## 執行紀錄 2 — Green（全部通過）

**執行指令**：
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**執行結果**：
```
test_parse_input_normal (test_task1.TestTask1SequenceClean) ... ok
test_dedupe_keep_order (test_task1.TestTask1SequenceClean) ... ok
test_sort_both_directions (test_task1.TestTask1SequenceClean) ... ok
test_filter_evens_with_negatives (test_task1.TestTask1SequenceClean) ... ok
test_parse_student (test_task2.TestTask2StudentRanking) ... ok
test_ranking_tie_break (test_task2.TestTask2StudentRanking) ... ok
test_top_k_exceeds_length (test_task2.TestTask2StudentRanking) ... ok
test_parse_log (test_task3.TestTask3LogSummary) ... ok
test_summarize_logs_basic (test_task3.TestTask3LogSummary) ... ok
test_empty_logs (test_task3.TestTask3LogSummary) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.008s

OK
```

**測試總數**：10　｜　**通過**：10　｜　**失敗**：0

**修改說明**：
完成上述三項修正後，所有測試全數通過；Task 3 補充了使用者同數時按名字升序排列的排序鍵，確保輸出穩定。