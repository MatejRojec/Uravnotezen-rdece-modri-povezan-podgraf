import random
from itertools import combinations

VZORCI = {
    1 :  [ [[1]] ],
    2 :  [ 
        [[[1]]], 
        [[[2]]], 
        [[[1, 2]]]],
    3 : [
        [[[1]]], 
        [[[2]]], 
        [[[3]]], 
        [[[1, 2]]], 
        [[[1], [3]]], 
        [[[1]], [[3]]], 
        [[[2, 3]]],
        [[[1, 2, 3]]]
    ],
    4 : [
        [[[1]]] ,
        [[[2]]] ,
        [[[3]]] ,
        [[[4]]] ,
        [[[1, 2]]],
        [[[1], [3]]],
        [[[1]], [[3]]],
        [[[1], [4]]],
        [[[1]], [[4]]],
        [[[2, 3]]],
        [[[2], [4]]],
        [[[2]], [[4]]],
        [[[3, 4]]],
        [[[1, 2, 3]]],
        [[[1, 2], [4]]],
        [[[1, 2]], [[4]]],
        [[[1], [3, 4]]],
        [[[1]], [[3, 4]]],
        [[[2, 3, 4]]],
        [[[1, 2, 3, 4]]]
    ]
}


class BCS:

    def __init__(self, G):
        self.G = G
        self.n = len(G) # st stolcev
        self.m = len(G[0]) # st vrstic
        a = [i for i in range(1, self.m)]
        sez = [i+1 for i in range(self.m)]
        # VZ = vsi mozni vzorci
        self.VZ = VZORCI[self.m]
        #self.VZ =  sum([list(map(list, combinations(sez, i))) for i in range(len(sez) + 1)], [])[1:]
    
    def vrednost_vzorca(self, vzorec, i): #vrednost vzorca v i-tem stolcu grafa G
        vsota = 0
        stolpec = self.G[i]
        if len(vzorec) == 1:
            vzorec = vzorec[0]
            vz  = list(set(sum(vzorec)))
            for el in vz:
                vsota += stolpec[el-1]
        else:   
            vz = []
            for el in vzorec:
                vz += el
            vz  = list(set(sum(vzorec)))
            for el in vz:
                vsota += stolpec[el-1]
        return(vsota)
    
    def generiraj_p_ijv(self): 
        self.p = []
        len_v = len(self.VZ)
        for i in range(self.n):
            self.p.append([])
            for j in range((2*self.n*self.m)+1): #
                self.p[i].append([[] for _ in range(len_v)])
        return(self.p)
    
    def generiraj_V(self): 
        self.V = []
        len_v = len(self.VZ)
        for i in range(self.n):
            self.V.append([])
            for j in range((2*self.n*self.m)+1): #
                self.V[i].append([[] for _ in range(len_v)])
        return(self.V)

# ustvari graf G
def generiraj_G(n, m, p): 
    # n...stevilo stolcev
    # m...stevilo vrstic
    # p...verjetnost redecega z vrednostjo 1
    vrednost = [1, -1]
    G = []
    for i in range(n):
        G.append(random.choices(vrednost, weights = [p, 1-p], k = m))
    return(G)
# Preveri ce se vzorec v1 ujema z vzorcem v2
def ujemanje(v1, v2): 
    for el in v2:
        if el in v1:
            return True
    return False
# Preveri povezanost vzorca
def povezan(vzorec): 
    if len(vzorec) == 1:
        return True
    else:
        i = vzorec[0]
        for el in vzorec:
            if i == el:
                pass
            else:
                return False
            i += 1
        return True


#  Poskus:
#g = generiraj_G(4, 3, 0.5)
#B = BCS(g)
#print(B.VZ)