# TEST CASES

| 編號 | 輸入（初始狀態 + 指令） | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式名稱 |
|---|---|---|---|---|---|
| 1 | `(1,1,N) + L` | 方向變 `W` | `W` | PASS | `test_turn_left_from_north_to_west` |
| 2 | `(1,1,N) + R` | 方向變 `E` | `E` | PASS | `test_turn_right_from_north_to_east` |
| 3 | `(1,1,S) + RRRR` | 回到 `S` | `S` | PASS | `test_four_right_turns_restore_direction` |
| 4 | `(5,3,N) + F` | 機器人 LOST | LOST | PASS | `test_forward_out_of_boundary_marks_lost` |
| 5 | `(1,1,E) + F` | 移到 `(2,1)` 且未 LOST | `(2,1)` | PASS | `test_forward_inside_boundary_moves_robot` |
| 6 | 第一台 `(5,3,N) + F` | 留下 `(5,3,N)` scent | 已留下 | PASS | `test_first_lost_robot_leaves_scent` |
| 7 | 第二台 `(5,3,N) + F` | 忽略危險 `F`，不 LOST | 留在原地 | PASS | `test_second_robot_ignores_dangerous_forward_with_same_scent` |
| 8 | 第二台 `(5,3,E) + F` | 不應共用北向 scent，應 LOST | LOST | PASS | `test_same_cell_different_direction_does_not_share_scent` |
| 9 | `(5,3,N) + FRF` | 第一步 LOST 後停止 | 不再轉向 | PASS | `test_lost_robot_stops_executing_later_commands` |
| 10 | `(0,0,N) + X` | 非法指令拋錯 | `ValueError` | PASS | `test_invalid_command_raises_value_error` |
| 11 | UVA: `(1,1,E) + RFRFRFRF` | 回到 `(1,1,E)` | 符合 | PASS | `test_sample_case_robot_one_matches_uva_118` |
| 12 | UVA: `(3,2,N) + FRRFLLFFRRFLL` | `(3,3,N) LOST` | 符合 | PASS | `test_sample_case_robot_two_matches_uva_118` |
| 13 | UVA: 前一台先留下 scent，再測 `(0,3,W) + LLFFFLFLFL` | `(2,3,S)` | 符合 | PASS | `test_sample_case_robot_three_uses_existing_scent` |