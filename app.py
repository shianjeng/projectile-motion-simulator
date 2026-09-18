"""Streamlit interface for the projectile-motion simulator."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from physics import SimulationResult, simulate_projectile


st.set_page_config(
    page_title="Projectile Motion Simulator",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Projectile Motion Simulator")
st.caption("空気抵抗を考慮した投射運動シミュレーター / Projectile motion with quadratic drag")

with st.sidebar:
    st.header("Simulation parameters")
    initial_speed = st.slider("Initial speed / 初速度 (m/s)", 5.0, 100.0, 40.0, 1.0)
    angle = st.slider("Launch angle / 投射角度 (°)", 1.0, 89.0, 45.0, 1.0)
    mass = st.slider("Mass / 質量 (kg)", 0.1, 10.0, 1.0, 0.1)
    drag = st.slider(
        "Drag coefficient k / 空気抵抗係数",
        0.0,
        0.10,
        0.015,
        0.001,
        format="%.3f",
    )
    time_step = st.select_slider(
        "Time step / 時間刻み (s)",
        options=[0.001, 0.002, 0.005, 0.01, 0.02],
        value=0.01,
    )


drag_result = simulate_projectile(
    initial_speed=initial_speed,
    angle_degrees=angle,
    mass=mass,
    drag_coefficient=drag,
    time_step=time_step,
)
vacuum_result = simulate_projectile(
    initial_speed=initial_speed,
    angle_degrees=angle,
    mass=mass,
    drag_coefficient=0.0,
    time_step=time_step,
)

metric_columns = st.columns(3)
metric_columns[0].metric("Flight time / 飛行時間", f"{drag_result.flight_time:.2f} s")
metric_columns[1].metric("Maximum height / 最大高度", f"{drag_result.max_height:.2f} m")
metric_columns[2].metric("Range / 水平到達距離", f"{drag_result.horizontal_range:.2f} m")

figure, axis = plt.subplots(figsize=(10, 5.5))
axis.plot(vacuum_result.x, vacuum_result.y, "--", linewidth=2, label="Without drag")
axis.plot(drag_result.x, drag_result.y, linewidth=2.5, label="With drag")
axis.set_xlabel("Horizontal distance x (m)")
axis.set_ylabel("Height y (m)")
axis.set_title("Projectile trajectory comparison")
axis.grid(alpha=0.25)
axis.legend()
axis.set_ylim(bottom=0)
st.pyplot(figure)


def result_to_dataframe(result: SimulationResult) -> pd.DataFrame:
    """Convert a simulation result to a table suitable for download."""

    return pd.DataFrame(
        {
            "time_s": result.time,
            "x_m": result.x,
            "y_m": result.y,
            "vx_m_s": result.vx,
            "vy_m_s": result.vy,
        }
    )


data = result_to_dataframe(drag_result)
with st.expander("Show simulation data / 計算データを表示"):
    st.dataframe(data, use_container_width=True)

st.download_button(
    "Download CSV / CSVをダウンロード",
    data=data.to_csv(index=False).encode("utf-8"),
    file_name="projectile_trajectory.csv",
    mime="text/csv",
)

st.info(
    "Model: quadratic drag  F = -k|v|v. "
    "The trajectory is calculated with the semi-implicit Euler method."
)
