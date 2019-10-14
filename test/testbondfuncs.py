import unittest
import qft.bondfuncs as bond


class TestBondFunctions(unittest.TestCase):
    def test_pv(self):
        self.assertAlmostEqual(bond.pv(1000, 100, 0.05, 2), 100/1.05+1100/1.05**2, places=3)


if __name__ == "__main__":
    unittest.main()