# Week 07 Homework - 赤壁戰役遊戲引擎

本作業實作一個簡化版三國赤壁戰役模擬器，整合 namedtuple、Counter、defaultdict、sorted 與檔案 I/O。

## 檔案

- generals.txt：9 位武將資料
- battles.txt：戰役設定
- solution/chibi_battle.py：完整版本
- solution/chibi_battle_easy.py：簡化執行入口
- solution/test_chibi.py：pytest 測試

## 執行方式

```bash
python solution/chibi_battle.py
python -m unittest solution.test_chibi -v
```