# %%
import numpy
import sympy
from necklace.eval.symp import evaluate, pi, symbol
from necklace.structures import (
    MickeyMouse,
    Necklace,
    NecklaceBodySolidAngleSum,
    NecklaceDihedralAngleSum,
    TeddyBear,
    Tripod,
)
from matplotlib import pyplot as plt


n = Necklace(body=0, head=1, beads=(3, 3, 3, 3, 3, 3, 3))


# %%


dihed_ang_sum = evaluate(NecklaceDihedralAngleSum(n)).simplify()
subs_dict = {
    symbol(0): 1,
    symbol(1): 1,
    symbol(2): 1,
}
solve_eq = dihed_ang_sum.subs(subs_dict) - 2 * pi
r3 = sympy.nsolve(solve_eq, symbol(3), (0.0001, 100), solver="bisect")
area_expr = evaluate(NecklaceBodySolidAngleSum(n))
area = area_expr.subs(subs_dict | {symbol(3): r3}).n(10)

# %%
r3
# %%
area

# %%


# %%
_.expand().together()
# %%
(area_expr.simplify().diff(symbol(1)).together())
# %%
num, denom = sympy.fraction(_)
# %%
num.expand()
# %%
denom.expand()

# %%
tr = Tripod()
