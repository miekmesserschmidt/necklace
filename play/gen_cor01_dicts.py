# %%
from collections import defaultdict
from pprint import pprint
import sympy
from necklace.compare import (
    Equal,
    Strict,
    corona_lower_bound,
    corona_upper_bound,
    mickey_mouse_lower_bound,
    mickey_mouse_upper_bound,
)
from necklace.gen import gen_all_mickey_mouses, gen_coronas, gen_mickey_mouse_dicts
from necklace.structures import Corona, CoronaAngleSum

# %%


# lower_b_comp = lambda m: mickey_mouse_lower_bound(m, smallest_r0=0.1010205144)
lower_b_comp = lambda m: mickey_mouse_lower_bound(m, smallest_r0=0.701)

mickey_mouses = set(map(lambda m: m.canonical(), gen_all_mickey_mouses({1}, {0, 1, 2})))
pprint(mickey_mouses)

lower_dict = {mm: lower_b_comp(mm) for mm in mickey_mouses}
upper_dict = {mm: mickey_mouse_upper_bound(mm) for mm in mickey_mouses}

# %%

d = defaultdict(int)
G = gen_mickey_mouse_dicts(d, mickey_mouses, lower_dict, upper_dict)


# %%
for g in G:
    print(g)
# %%
