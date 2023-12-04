# %%
from itertools import chain
import sympy
from necklace.compute.mickey_mouse import angle
from necklace.poly.tools import ensure_square_of_sub_expressions
from necklace.structures import Corona
from necklace.environs.sympy_env import env
from necklace.compute import corona, mickey_mouse
import multiprocessing

# %%


c = Corona(
    0,
    (1, 2, 3),
)
cos_symbols = list(corona.cos_variables(c, env))
sin_symbols = list(corona.sin_variables(c, env))
rad_symbols = list(corona.radii_variables(c, env))

cos_symbols.sort(key=lambda s: str(s))
sin_symbols.sort(key=lambda s: str(s))
rad_symbols.sort(key=lambda s: str(s))

print(rad_symbols)
r0, r1, r2, *rest = rad_symbols

# %%
subs_dict = {
    env.symbol_map(m): angle(m, env).expand() for m in set(c.mickey_mouse_sequence())
}
# %%
eq = corona.equation(c, env)
print("expand trig")
eq = sympy.expand_trig(eq).expand()

sin = env.sin
cos = env.cos
sin_cos_eqs = [
    sin(env.symbol_map(m)) ** 2 + cos(env.symbol_map(m)) ** 2 - 1
    for m in set(c.mickey_mouse_sequence())
]
mickey_mouse_system = [
    mickey_mouse.equation(m, env) for m in set(c.mickey_mouse_sequence())
]


# eq = ensure_square_of_sub_expressions(eq, sin_symbols)
print("trig system")
trig_system = [eq] + sin_cos_eqs
# %%
print("trig system, remove odd powers of sin")
no_odd_power_trig_system = [
    ensure_square_of_sub_expressions(eq, sin_symbols)
] + sin_cos_eqs


# %%
def whole_mon_order(degree_list: list[int]):
    sins = degree_list[: len(sin_symbols)]
    coss = degree_list[len(sin_symbols) : len(sin_symbols) + len(cos_symbols)]
    rs = degree_list[len(sin_symbols) + len(cos_symbols) :]

    sins_tup = tuple(-i for i in reversed(sins))
    coss_tup = tuple(-i for i in reversed(coss))
    # rs_tup = tuple(-i for i in reversed(rs))
    rs_tup = tuple(rs)

    return (sum(sins), sins_tup, sum(coss), coss_tup, sum(rs), rs_tup)


# %%
# Gtrig = sympy.groebner(
#     trig_system, *(sin_symbols + cos_symbols + rad_symbols), order=whole_mon_order
# )
# for p in Gtrig:
#     print(p)

# %%
Gtrig = sympy.groebner(
    no_odd_power_trig_system,
    *(sin_symbols + cos_symbols + rad_symbols),
    order=whole_mon_order,
)
for p in Gtrig:
    print(p)
# %%


# %%
P = Gtrig[-1].factor().args[0]
P = P.subs(subs_dict)
P
# %%
P = P.together()
P, _ = sympy.fraction(P)
P
# %%


def worker(t):
    return t.expand()


result = 0
with multiprocessing.Pool(10) as pool:
    for i, t in enumerate(pool.imap_unordered(worker, P.args)):
        print(i)
        result += t

    P = result.factor()
# %%


# %%
P
# %%
P = result.factor()
# %%
print(P.args[-1])
# %%
