def bootstrap_rate(fv, pmt, nper, s_n):
    return ((pmt + fv)/fv*(1+s_n)**nper)**(1/(nper+1)) - 1


def floating_pv(fv, pmt, spots):
    return sum(pmt/(1+r)**(n+1) for n, r in enumerate(spots)) \
           + fv/(1+spots[-1])**len(spots)
