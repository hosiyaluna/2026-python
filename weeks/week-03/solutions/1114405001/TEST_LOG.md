# TEST LOG

## Red

- 指令：`python -m unittest discover -s tests -p "test_*.py" -v`
- 結果摘要：尚未實作 `robot_core.py` 時，核心規則測試無法通過。
- 測試總數 / 通過 / 失敗：15 / 0 / 15
- 修正摘要：先建立 `RobotWorld`、`Robot`、旋轉與前進規則，再補上 `scent` 與 `LOST` 停止邏輯。

## Green

- 指令：`python -m unittest discover -s tests -p "test_*.py" -v`
- 結果摘要：全部測試通過。
- 測試總數 / 通過 / 失敗：15 / 15 / 0
- 修正摘要：確保 `scent` 以 `(x, y, dir)` 記錄，並驗證 UVA 118 三組經典案例。