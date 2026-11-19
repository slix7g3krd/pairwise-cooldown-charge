import pytest
from gameplay import cooldown_charge as mod

CASES = [
    ("time_half", 'm.scaled_time(1.0, 0.5) == approx(0.5)'),
    ("time_zero", 'm.scaled_time(1.0, 0.0) == approx(0.0)'),
    ("charge_half", 'm.charge_fraction(1.0, 2.0) == approx(0.5)'),
    ("charge_full", 'm.charge_fraction(2.0, 2.0) == approx(1.0)'),
    ("reduction_sum", 'm.cooldown_reduction(10.0, [2.0, 3.0]) == approx(5.0)'),
    ("reduction_floor", 'm.cooldown_reduction(1.0, [2.0]) == approx(0.0)'),
    ("refund", 'm.refund_on_fail(10.0, 5.0) == approx(15.0)'),
    ("segment_pair", 'm.segment_key(7, 2) == (7, 2)'),
    ("restore", 'm.restore_event(3, 2) == 5'),
    ("server_latency", 'm.server_remaining(10.0, 2.0) == approx(8.0)'),
    ("death_zero", 'm.death_scale(True) == approx(0.0)'),
    ("alive_one", 'm.death_scale(False) == approx(1.0)'),
    ("weapon_pair", 'm.weapon_key(3, 7) == (3, 7)'),
    ("fixed_half", 'm.fixed_step(0.6, 0.5) == approx(0.5)'),
    ("fixed_zero", 'm.fixed_step(0.0, 0.5) == approx(0.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
