from qft.qft import solve_pv, solve_fv, solve_pmt, solve_rate, solve_nper
import unittest
import math


class TestBondFunctions(unittest.TestCase):
    def test_bond_functions(self):
        fv, pmt, rate, nper, pv = 1000, 100, 0.05, 2, -(100/1.05 + 1100/1.05**2)
        assert math.isclose(pv, solve_pv(fv, pmt, rate, nper))
        assert math.isclose(fv, solve_fv(pv, pmt, rate, nper))
        assert math.isclose(pmt, solve_pmt(pv, fv, rate, nper))
        assert math.isclose(rate, solve_rate(pv, fv, pmt, nper))
        assert math.isclose(nper, solve_nper(pv, fv, pmt, rate))


if __name__ == "__main__":
    unittest.main()
