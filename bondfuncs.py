

def pv(fv, pmt, rate, nper):
    return pmt*(1-(1+rate)**(-nper))/rate + fv*(1+rate)**(-nper)

