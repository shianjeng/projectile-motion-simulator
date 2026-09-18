"""Generate the demonstration image used in the README."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from physics import simulate_projectile  # noqa: E402


vacuum = simulate_projectile(40.0, 45.0, drag_coefficient=0.0)
with_drag = simulate_projectile(40.0, 45.0, drag_coefficient=0.015)

plt.style.use("seaborn-v0_8-whitegrid")
figure, axis = plt.subplots(figsize=(10, 5.5))
axis.plot(vacuum.x, vacuum.y, "--", linewidth=2.2, label="Without air resistance")
axis.plot(with_drag.x, with_drag.y, linewidth=2.8, label="With air resistance")
axis.scatter([with_drag.x[-1]], [0], color="#d1495b", zorder=3)
axis.set(
    title="Projectile Motion Simulator",
    xlabel="Horizontal distance x (m)",
    ylabel="Height y (m)",
    ylim=(0, None),
)
axis.legend()
figure.tight_layout()
figure.savefig(PROJECT_ROOT / "assets" / "demo.png", dpi=160)
