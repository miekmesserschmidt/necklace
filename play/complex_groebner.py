# %%

from typing import Tuple

import sympy
from necklace.compute.corona import (
    angle_variables,
    generalized_root_of_unity_equation,
    complex_system,
    complex_variables,
)
from necklace.environs import sympy_env
from necklace.structures import Corona

env = sympy_env.env

# %%
c = Corona(0, (1, 2, 3, 4, 5))

# %%
system = complex_system(c, env)

complex_vars = complex_variables(c, env)
angle_vars = angle_variables(c, env)
cos_vars = [env.cos(a) for a in angle_vars]


# %%
def monomial_order(power_list) -> Tuple:
    cvars = power_list[: len(complex_vars)]
    cos_ = power_list[len(complex_vars) : len(complex_vars) + len(cos_vars)]

    # cvar_weight = sum(i * c for i, c in enumerate(cvars, start=2))
    cvar_weight = sum(cvars)

    return (cvar_weight, tuple(cvars), sum(cos_), tuple(cos_))


# %%


system
# %%
cos_vars
# %%
complex_vars
# %%
monomial_order([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# %%
G = sympy.groebner(
    system, *(complex_vars + cos_vars), order=monomial_order, method="f5b"
)
# %%

for p in G:
    print(p)

# %%
G[-1].factor()
# %%
