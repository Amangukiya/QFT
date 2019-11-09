from sympy import symbols, solve

pv, fv, pmt, nper, rate = symbols("pv fv pmt nper rate")
expr = pv + pmt*(1 - (1 + rate)**-nper)/rate + fv*(1 + rate)**-nper


def solve_pv(fv, pmt, nper, rate):
    return solve(expr.subs({"fv": fv, "pmt": pmt, "rate": rate, "nper": nper}), pv)[0]


def solve_fv(pv, pmt, nper, rate):
    return solve(expr.subs({"pv": pv, "pmt": pmt, "rate": rate, "nper": nper}), fv)[0]


def solve_pmt(pv, fv, nper, rate):
    return solve(expr.subs({"pv": pv, "fv": fv, "rate": rate, "nper": nper}), pmt)[0]


def solve_nper(pv, fv, pmt, rate):
    return next(x for x in solve(expr.subs({"pv": pv, "fv": fv, "pmt": pmt, "rate": rate}), nper) if x >= 0)


def solve_rate(pv, fv, pmt, nper):
    return next(x for x in solve(expr.subs({"pv": pv, "fv": fv, "pmt": pmt, "nper": nper}), rate) if x >= 0)

