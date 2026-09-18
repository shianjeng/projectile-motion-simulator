"""Physics calculations for two-dimensional projectile motion."""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np


@dataclass(frozen=True)
class SimulationResult:
    """Time-series data and summary metrics for one trajectory."""

    time: np.ndarray
    x: np.ndarray
    y: np.ndarray
    vx: np.ndarray
    vy: np.ndarray
    flight_time: float
    max_height: float
    horizontal_range: float


def simulate_projectile(
    initial_speed: float,
    angle_degrees: float,
    mass: float = 1.0,
    drag_coefficient: float = 0.0,
    time_step: float = 0.01,
    gravity: float = 9.80665,
    max_time: float = 120.0,
) -> SimulationResult:
    """Simulate a projectile with quadratic air resistance.

    The drag acceleration is ``-(k / m) * |v| * v``. A semi-implicit Euler
    method is used because it is simple to explain and stable enough for this
    educational application.
    """

    _validate_inputs(
        initial_speed,
        angle_degrees,
        mass,
        drag_coefficient,
        time_step,
        gravity,
        max_time,
    )

    angle_radians = math.radians(angle_degrees)
    x = 0.0
    y = 0.0
    vx = initial_speed * math.cos(angle_radians)
    vy = initial_speed * math.sin(angle_radians)
    current_time = 0.0

    times = [current_time]
    xs = [x]
    ys = [y]
    vxs = [vx]
    vys = [vy]

    while current_time < max_time:
        speed = math.hypot(vx, vy)
        ax = -(drag_coefficient / mass) * speed * vx
        ay = -gravity - (drag_coefficient / mass) * speed * vy

        vx += ax * time_step
        vy += ay * time_step
        next_x = x + vx * time_step
        next_y = y + vy * time_step
        next_time = current_time + time_step

        if next_y < 0.0 and current_time > 0.0:
            fraction = y / (y - next_y)
            landing_time = current_time + fraction * time_step
            landing_x = x + fraction * (next_x - x)
            landing_vx = vxs[-1] + fraction * (vx - vxs[-1])
            landing_vy = vys[-1] + fraction * (vy - vys[-1])

            times.append(landing_time)
            xs.append(landing_x)
            ys.append(0.0)
            vxs.append(landing_vx)
            vys.append(landing_vy)
            break

        current_time = next_time
        x = next_x
        y = next_y
        times.append(current_time)
        xs.append(x)
        ys.append(y)
        vxs.append(vx)
        vys.append(vy)
    else:
        raise RuntimeError("Projectile did not land before max_time.")

    time_array = np.asarray(times)
    x_array = np.asarray(xs)
    y_array = np.asarray(ys)
    vx_array = np.asarray(vxs)
    vy_array = np.asarray(vys)

    return SimulationResult(
        time=time_array,
        x=x_array,
        y=y_array,
        vx=vx_array,
        vy=vy_array,
        flight_time=float(time_array[-1]),
        max_height=float(np.max(y_array)),
        horizontal_range=float(x_array[-1]),
    )


def _validate_inputs(
    initial_speed: float,
    angle_degrees: float,
    mass: float,
    drag_coefficient: float,
    time_step: float,
    gravity: float,
    max_time: float,
) -> None:
    if initial_speed <= 0:
        raise ValueError("initial_speed must be positive")
    if not 0 <= angle_degrees <= 90:
        raise ValueError("angle_degrees must be between 0 and 90")
    if mass <= 0:
        raise ValueError("mass must be positive")
    if drag_coefficient < 0:
        raise ValueError("drag_coefficient cannot be negative")
    if time_step <= 0:
        raise ValueError("time_step must be positive")
    if gravity <= 0:
        raise ValueError("gravity must be positive")
    if max_time <= 0:
        raise ValueError("max_time must be positive")
