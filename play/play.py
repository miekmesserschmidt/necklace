# %%

import sympy
from necklace.compute.corona import matrix, triangle_matrix
from necklace.compute.mickey_mouse import all_mickey_mouses, angle, cos_angle
from necklace.compute.triangle import all_triangles
from necklace.structures import Corona, MickeyMouse, Necklace
from necklace.environs.sympy_env import env

# %%
r0, r1, r2, r3, *_ = (env.symbol_map(i) for i in range(100))

subs_dict = {r0: 1, r1: 1.1, r3: 0.4}

# %%

m = MickeyMouse(0, 1, 2)
# %%
cos_angle(m, env)
# %%
# %%

c0 = Corona(0, (1, 1, 1, 0, 0))
c1 = Corona(1, (1, 1, 0, 0, 1, 1, 0))

mms = list(all_mickey_mouses([0, 1]))
mms.sort()

M0 = matrix(c0, mms)
M1 = matrix(c1, mms)

T = triangle_matrix(mms)

# %%
M.rref()[0][:, :-1]
# %%
M
# %%
M.nullspace()[0].dot(M.nullspace()[1])
# %%
M0.rref()[0][:, :-1].nullspace()

# %%
M1
# %%
