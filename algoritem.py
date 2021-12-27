import random
import itertools
from itertools import combinations

# GENERIRANJE MREŽ

mylist=[1,-1]

def mreza(stol, vrst):
	all_nodes=[]
	for x in range(stol):
		for y in range(vrst):
			all_nodes.append([x,y, random.choice(mylist)])
	return all_nodes

# print (mreza(2,3))     vrne [stolpec, element v stolpcu, barva R=1 M=-1]
m1 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1], [2, 0, 1], [2, 1, -1]]

# OSNOVNE FUNKCIJE

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

def j_vzorca(mreza, vzorec, stolpec):
    j = 0
    for item in mreza:
        if item[0] == stolpec:
            for v in vzorec:
                if item[1] == (v-1):
                    j = j+item[2]
    return j

# GLAVNA FUNKCIJA

def pji(mreza):        #nam da prazen seznam ki ga bomo polnili [[[[]*st_vzorcev]*j]*st_stolpcev]
    p = []
    for i in range(st_stolpcev(mreza)):
        p.append([])
        for j in range((2*(i+1)*st_vrstic(mreza))+1):
            p[i].append([[] for _ in range(len(vzorec(mreza)))])
    return p

def alg(mreza):
    p = pji(mreza)
    for i in range(st_stolpcev(mreza)):
        meja_j = (i+1)*st_vrstic(mreza)
        if i == 0:
            for j in range(2*meja_j+1):
                c = j-2
                for v in range(len(vzorec(mreza))):
                    vzr = (vzorec(mreza))[v]
                    if j_vzorca(mreza, vzr, i) == c:
                        p[i][j][v] = len(set(vzr))
                    else:
                        p[i][j][v] = float('-inf')
    return (p)

            
print(alg(m1))

