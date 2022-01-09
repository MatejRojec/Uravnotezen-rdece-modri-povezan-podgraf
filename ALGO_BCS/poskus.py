import random
from itertools import combinations, permutations

u = [[[1]]]
v = [[[1]],[[3]]]
du = [set(sum(d, [])) for d in u] # deli u
vv = set(sum(sum(v, []),[])) # množica vozlišč v
pogoj1 = all(any(x in vv for x in d) for d in du)
pogoj2 = all(any(all(any(x in c for x in e) for c in d) for e in du) for d in v if len(d) > 1)

result = []
lists =  [[[1], [3]]]

for list1 in lists:
    for j in list1:
        for l in j:
            result.append(l)