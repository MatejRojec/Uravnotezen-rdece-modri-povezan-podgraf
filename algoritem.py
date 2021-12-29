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
m2 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1]]

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

def ujemanje(v1, v2):
    for el in v2:
        if el in v1:
            return True
    return False
    
# GLAVNA FUNKCIJA

def pji(mreza):        #nam da prazen seznam ki ga bomo polnili [[[[]*st_vzorcev]*j]*st_stolpcev]
    p = []
    for i in range(st_stolpcev(mreza)):
        p.append([])
        for j in range((2*st_stolpcev(mreza)*st_vrstic(mreza))+1):
            p[i].append([[] for _ in range(len(vzorec(mreza)))])
    return p


def pijv(mreza, p, i, j, v):    #TO DELA OK/ JE DELALO :)
    a = [0]
    vsota_v = j_vzorca(mreza, v, i)
    b = j-vsota_v
    if b == 0:
        a.append(len(set(v)))
    for u in range(len(vzorec(mreza))):
        vzr = (vzorec(mreza))[u]
        if ujemanje(vzr, v):
            a.append(len(set(v))+p[i-1][b+st_stolpcev(mreza)*st_vrstic(mreza)][u])
    return max(a)    


def alg(mreza):

    p = pji(mreza)
    stol = st_stolpcev(mreza)
    vrst = st_vrstic(mreza)

    for i in range(stol): 
        for j in range((2*stol*vrst)+1): 
            for v in range(len(vzorec(mreza))):
                vzr = (vzorec(mreza))[v]

                if i == 0:  #postavimo vse p za prvi stolpec
                    if j_vzorca(mreza, vzr, i) == j - stol*vrst:
                        p[i][j][v] = j_vzorca(mreza, vzr, i)
                    else:
                        p[i][j][v] = float('-inf')
                
                elif j > (i+1)*vrst+vrst*stol or j < -(i+1)*vrst+vrst*stol: #postavimo vse p kjer |j| > i|G| na -inf
                    p[i][j][v] = float('-inf')
                
                else:
                    p[i][j][v] = pijv(mreza,p, i+1, 0, vzr)
 
                    
                


        # else:
        #     # for j in range(2*meja_j+1):
        #     #     c = j-i*st_vrstic(mreza)-1
        #     #     for v in range(len(vzorec(mreza))):
        #     #         vzr = (vzorec(mreza))[v]
        #     #         p[i][j][v] = len(vzorec(mreza))
    return (p)

            
print(alg(m1))


# print(pijv(m1,alg(m1),1, -1, [1,2]))
# print(pijv(m1,alg(m1),1, 0, [1,2]))
# print(pijv(m1,alg(m1),1, 1, [1,2]))
# print(pijv(m1,alg(m1),1, -1, [1]))