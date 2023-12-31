# %%

from functools import cache
import sympy
from necklace.compute import corona
from necklace.compute import mickey_mouse
from necklace.compute.corona import matrix, triangle_matrix
from necklace.compute.mickey_mouse import all_mickey_mouses, angle, cos_angle
from necklace.compute.triangle import all_triangles
from necklace.structures import Corona, MickeyMouse, Necklace
from necklace.environs.sympy_env import env


# %%


def cosine_rec(ws: tuple):
    if len(ws) == 1:
        return sympy.cos(ws[0])
    else:
        w0, *w_rest = ws
        cos_rest = cosine_rec(w_rest)
        return -2 * sympy.cos(w0) * cos_rest + sympy.cos(w0) ** 2 + cos_rest**2


# %%


def _rec(index: int, symbol_map):
    if index == 0:
        return symbol_map(index)
    else:
        w = symbol_map(index)
        w_rest = _rec(index - 1, symbol_map).expand()
        return w**2 + w_rest**2 - 2 * w * w_rest


# %%
def w(index):
    return sympy.symbols(f"w_{index}")


# %%
result = _rec(10, w)
# %%
print(result.expand())
# %%
print(result)
# %%
