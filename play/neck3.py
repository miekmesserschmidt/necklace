# %%
import numpy
import sympy
from necklace.compute.computer import DefaultComputer
from necklace.structures import MickeyMouse, Necklace, TeddyBear
from matplotlib import pyplot as plt

comp = DefaultComputer()

n = Necklace(body=0, head=1, beads=(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3))
t = TeddyBear(body=0, head=1, hand0=2, hand1=3)
m = MickeyMouse(head=0, ear0=1, ear1=2)
# %%


ang_sum = comp.compute(n)
r = [comp.compute(i) for i in range(10)]


# %%
n_angsum = comp.compute(n)

# %%
# %%

R1 = numpy.linspace(0.1, 2, 100)
R3 = []

for r1 in R2:

    A = n_angsum.subs(
        {
            r[0]: 1,
            r[1]: r1,
            # r[2]: r2,
        }
    )
    r3 = sympy.nsolve(A - 2 * sympy.pi, (r[3],), 0.1, prec=50)
    print(r3)
    R3.append(sympy.Abs(r3))

# %%
plt.plot(R2, R3)

# smaller r5
# %%

t23 = TeddyBear(body=0, head=1, hand0=2, hand1=3)
t34 = TeddyBear(body=0, head=1, hand0=3, hand1=4)
t24 = TeddyBear(body=0, head=1, hand0=2, hand1=4)

# %%
comp.compute(t24) >= comp.compute(t23) + comp.compute(t34)
# %%
sympy.simplify(_)
# %%
((1 / (sympy.sqrt(3) + 2)) / sympy.sqrt(3)).n(10)
# %%
R2
# %%
R3
# %%
plt.plot(R2, R3)
# %%
