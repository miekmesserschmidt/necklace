# %%
from collections import defaultdict
from pprint import pprint
import sympy
from necklace.compare import Equal, Strict, corona_lower_bound, corona_upper_bound
from necklace.gen import gen_coronas
from necklace.structures import Corona, CoronaAngleSum

# %%


lower_b_comp = lambda cor: corona_lower_bound(cor, smallest_r0=0.1010205144)


G = gen_coronas(Corona(1, tuple()), {0, 1, 2}, lower_bound_computer=lower_b_comp)
results = defaultdict(list)
for cor in G:
    print(cor)
    results[CoronaAngleSum(cor.canonical())].append(cor)

# %%
pprint(list(results.keys()))
# %%
len(results)
# %%


# %%
# %%
list(results.keys())
# %%
c0 = Corona(center=0, seq=(1, 0, 0, 0, 0, 0))
corona_lower_bound(c0)
# %%
