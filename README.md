# Projectile Motion Simulator

[日本語](#日本語) | [English](#english)

![Trajectory comparison](assets/demo.png)

## 日本語

### プロジェクト概要

物理学で学ぶ投射運動を題材に、空気抵抗の有無による軌道の違いを可視化する
Pythonアプリケーションです。初速度、投射角度、質量、空気抵抗係数を変更し、
飛行時間・最大高度・水平到達距離をインタラクティブに確認できます。

このプロジェクトでは、二次空気抵抗
`F = -k|v|v` をモデル化し、半陰的オイラー法を用いて運動方程式を数値的に
解いています。

### 主な機能

- 空気抵抗あり／なしの軌道比較
- 初速度、角度、質量、空気抵抗係数の変更
- 飛行時間、最大高度、水平到達距離の計算
- 計算結果の表形式表示
- シミュレーションデータのCSV出力
- `pytest`による計算ロジックの自動テスト

### 使用技術

- Python
- NumPy / Pandas
- Matplotlib
- Streamlit
- Pytest / GitHub Actions

### 実行方法

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

ブラウザで `http://localhost:8501` を開いてください。

### テスト

```bash
pytest -q
```

### 学んだこと

- 物理モデルをプログラムへ落とし込む方法
- 数値計算と解析解の比較
- 計算ロジックとUIを分離したコード設計
- データ可視化とCSV出力
- GitHub Actionsによる自動テスト

## English

### Overview

An interactive Python application that visualizes projectile motion with and
without quadratic air resistance. Users can change the initial speed, launch
angle, mass, and drag coefficient, then inspect the trajectory and summary
metrics.

The model uses the quadratic drag force `F = -k|v|v` and solves the equations
of motion numerically with the semi-implicit Euler method.

### Features

- Compare trajectories with and without air resistance
- Interactive simulation parameters
- Calculate flight time, maximum height, and horizontal range
- Inspect the time-series data
- Export results as CSV
- Automated tests for the physics calculation

### Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### Repository structure

```text
.
├── app.py                 # Streamlit user interface
├── physics.py             # Simulation logic
├── tests/                 # Automated tests
├── scripts/               # Utility scripts
├── assets/demo.png        # Demonstration image
└── requirements.txt       # Python dependencies
```

## Author

Xianzheng Zhu  
GitHub: https://github.com/shianjeng