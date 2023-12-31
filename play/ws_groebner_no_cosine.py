# %%

import sympy
from necklace.compute import corona
from necklace.compute import mickey_mouse
from necklace.compute.corona import matrix, triangle_matrix
from necklace.compute.mickey_mouse import all_mickey_mouses, angle, cos_angle
from necklace.compute.triangle import all_triangles
from necklace.structures import Corona, MickeyMouse, Necklace
from necklace.environs.sympy_env import env

# %%
n = 5

c = Corona(0, range(1, n + 1))

R = list(map(env.symbol_map, sorted(c.labels)))

ALL_MMs = list(c.mickey_mouse_sequence(canonical=False))
W = [mickey_mouse.complex_(m, env) for m in ALL_MMs]
Z = [mickey_mouse.complex_multiplier(m, env) for m in ALL_MMs]


# MMs = ALL_MMs
MMs = ALL_MMs
cos_rules = [mickey_mouse.cosine_rule_equation(m, env) for m in MMs]
unit_circle_rules = [mickey_mouse.on_complex_unit_circle_equation(m, env) for m in MMs]
corona_root_rules = [corona.generalized_root_of_unity_equation(c, env)]
corona_root_sq_rules = [corona.generalized_root_of_unity_equation_sq(c, env)]
# %%
Z
# %%

cos_rules
# %%
unit_circle_rules
# %%
corona_root_rules


# %%
G = sympy.groebner(
    (corona_root_rules + unit_circle_rules),
    # (unit_circle_rules + cos_rules + corona_root_sq_rules),
    *(cosA + W),
    # order=
    # method="f5b",
)

# %%
H = sympy.groebner(
    (cos_rules),
    # (unit_circle_rules + cos_rules + corona_root_sq_rules),
    *(cosA + R),
    # order=
    # method="f5b",
)

# %%
for g in H:
    print(g, "\n")

# %%
G.reduce(cos_rules[0])
# %%
len(H)
# %%
