from abc import abstractmethod, ABCMeta
from typing import Mapping, Callable
import more_itertools
from qft.qft import solve_pv


def pv(fv: float, rate: float, t: float) -> float:
    return fv*(1+rate)**-t


class Bond(metaclass=ABCMeta):
    def __init__(self, par: float, pmt: float):
        self.par = float(par)
        self.pmt = float(pmt)

    @abstractmethod
    def get_spot(self, t: float) -> float:
        raise NotImplementedError

    def flow(self, n: int, compounds: int = 1) -> float:
        return - pv(self.pmt / compounds, self.get_spot(n / compounds) / compounds, n)

    def final_flow(self, n: int, compounds: int = 1) -> float:
        return - pv(self.par, self.get_spot(n) / compounds, compounds * n)

    def pv(self, maturity: int, compounds: int = 1) -> float:
        return sum(self.flow(n+1, compounds) for n in range(compounds * maturity)) \
               + self.final_flow(maturity, compounds)


class FlatBond(Bond):
    def __init__(self, par: float, pmt: float, rate: float):
        super().__init__(par, pmt)
        self.rate = float(rate)

    def get_spot(self, t: float) -> float:
        return self.rate

    def pv(self, maturity: int, compounds: int = 1) -> float:
        return solve_pv(self.par, self.pmt / compounds,
                        maturity * compounds, self.rate / compounds)


class InterpolatedBond(Bond):
    def __init__(self, par: float, pmt: float, spots: Mapping[float, float]):
        super().__init__(par, pmt)
        # todo: make it easier so you can put in a list? (but then does it start at 0 or 1)
        self.spots = {float(k): float(v) for k, v in spots}

    def get_spot(self, t: float) -> float:
        if not self.spots:
            raise RuntimeError("Cannot interpolate without spot rates")
        elif t in self.spots:
            return self.spots[t]
        else:
            groups = more_itertools.bucket(self.spots.keys(), key=lambda x: x > t)
            L = max(groups[False], default=None)  # closest key on the left
            R = min(groups[True], default=None)  # closest key on the right
            if L is None:  # if none are smaller
                return self.spots[R]  # flat interpolation
            elif R is None:  # if none are bigger
                return self.spots[L]  # flat interpolation
            else:
                m = (self.spots[R] - self.spots[L]) / (R - L)  # get slope
                return m * (t - L) + self.spots[L]  # linear interpolation


class CurvedBond(Bond):
    def __init__(self, par: float, pmt: float, f: Callable[[float], float]):
        super().__init__(par, pmt)
        self.f = f

    def get_spot(self, t: float) -> float:
        return self.f(t)
