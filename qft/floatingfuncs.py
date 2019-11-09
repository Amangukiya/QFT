def bootstrap_rate(fv, pmt, nper, s_n):
    """
    fv: future value
    pmt: payment
    nper: num periods 
    s_n: spot rate at period n
    --
    returns s_(n+1)
    """
    return ((pmt + fv)/fv*(1+s_n)**nper)**(1/(nper+1)) - 1


def floating_pv(fv, pmt, spots):
    return sum(pmt/(1+r)**(n+1) for n, r in enumerate(spots)) \
           + fv/(1+spots[-1])**len(spots)
