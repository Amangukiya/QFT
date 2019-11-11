from qft import solve_pv, FlatBond, InterpolatedBond, CurvedBond
from hypothesis import given, strategies as st
import unittest
import math


clean_floats = st.floats(1.0, 100.0, allow_nan=False, allow_infinity=False)


class TestFlatBond(unittest.TestCase):
    @given(par=clean_floats, pmt=clean_floats, rate=clean_floats)
    def test_flat_bond_rate(self, par, pmt, rate):
        bond = FlatBond(par, pmt, rate)
        self.assertEqual(bond.rate, rate)

    @given(par=clean_floats, pmt=clean_floats, rate=clean_floats,
           maturity=st.integers(1, 100), compounds=st.integers(1, 100))
    def test_flat_bond_pv(self, par, pmt, rate, maturity, compounds):
        pv1 = FlatBond(par, pmt, rate).pv(maturity, compounds)
        pv2 = solve_pv(par, pmt/compounds, maturity*compounds, rate/compounds)
        assert math.isclose(pv1, pv2)


# todo: tests for interpolated and curved bond

if __name__ == "__main__":
    unittest.main()
