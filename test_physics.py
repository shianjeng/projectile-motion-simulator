import math

import numpy as np
import pytest

from physics import simulate_projectile


def test_no_drag_matches_analytical_range() -> None:
    speed = 30.0
    angle = 45.0
    gravity = 9.80665
    expected_range = speed**2 * math.sin(math.radians(2 * angle)) / gravity

    result = simulate_projectile(
        initial_speed=speed,
        angle_degrees=angle,
        drag_coefficient=0.0,
        gravity=gravity,
        time_step=0.001,
    )

    assert result.horizontal_range == pytest.approx(expected_range, rel=0.002)


def test_drag_reduces_range() -> None:
    vacuum = simulate_projectile(40.0, 45.0, drag_coefficient=0.0)
    with_drag = simulate_projectile(40.0, 45.0, drag_coefficient=0.015)

    assert with_drag.horizontal_range < vacuum.horizontal_range
    assert with_drag.max_height < vacuum.max_height


def test_trajectory_starts_and_ends_at_ground() -> None:
    result = simulate_projectile(20.0, 35.0, drag_coefficient=0.01)

    assert result.y[0] == 0.0
    assert result.y[-1] == 0.0
    assert np.all(result.y >= 0.0)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"initial_speed": 0.0, "angle_degrees": 45.0},
        {"initial_speed": 20.0, "angle_degrees": -1.0},
        {"initial_speed": 20.0, "angle_degrees": 91.0},
        {"initial_speed": 20.0, "angle_degrees": 45.0, "mass": 0.0},
        {"initial_speed": 20.0, "angle_degrees": 45.0, "drag_coefficient": -0.1},
    ],
)
def test_invalid_inputs_raise_value_error(kwargs: dict[str, float]) -> None:
    with pytest.raises(ValueError):
        simulate_projectile(**kwargs)
