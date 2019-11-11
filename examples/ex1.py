from qft import FlatBond, CurvedBond
import matplotlib.pyplot as plt


for i in range(1, 11):
    b = FlatBond(par=100, pmt=10, rate=0.02*i)
    plt.plot(list(-b.pv(maturity=m+1) for m in range(20)))

plt.xlabel("maturity")
plt.ylabel("present value")
plt.show()