import random
import itertools
from itertools import combinations

mylist=[1,-1]

def mreza(stol, vrst):
	all_nodes=[]
	for x in range(stol):
		for y in range(vrst):
			all_nodes.append([x,y, random.choice(mylist)])
	return all_nodes

# print (mreza(2,3))     vrne [stolpec, element v stolpcu, barva R=1 M=-1]
m1 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1], [2, 0, 1], [2, 1, -1]]

def vzorec(mreza):
    a = [item[1] for item in mreza]
    st_vrstic = len(set(a))
    l = [i+1 for i in range(st_vrstic)]
    return sum([list(map(list, combinations(l, i))) for i in range(len(l) + 1)], [])

print(vzorec(m1))   # --> particija stolpca v mrezi [[], [1], [2], [1, 2]]

def st_vrstic(mreza):
    a = [item[1] for item in mreza]
    return len(set(a))

def st_stolpcev(mreza):
    a = [item[0] for item in mreza]
    return len(set(a))

def pji(mreza):        #nam da prazen seznam ki ga bomo polnili [[[[]*st_vzorcev]*j]*st_stolpcev]
    p = []
    for i in range(st_stolpcev(mreza)):
        p.append([])
        for j in range((2*(i+1)*st_vrstic(mreza))+1):
            p[i].append([[] for _ in range(len(vzorec(mreza)))])
    return p

print(pji(m1))

def alg(mreza):
    p = pji(mreza)
    

print(alg(m1))
