import random
from itertools import combinations


class BCS:

    def __init__(self, G):
        self.G = G
        self.n = G[0] # st stolcev
        self.m = G[1] # st vrstic
        a = [i for i in range(1, self.m)]
        sez = [i+1 for i in range(self.m)]
        self.V =  sum([list(map(list, combinations(sez, i))) for i in range(len(sez) + 1)], [])[1:]


    def vrednost_vzorca(self, vzorec, i): #vrednost vzorca v i-tem stolcu grafa G
        vsota = 0
        stolpec = self.G[i]
        for el in vzorec:
            vsota += stolpec[el-1]
        return(vsota)

    def generiraj_p_ijv(self): 
        self.p = []
        len_v = len(self.V)
        for i in range(self.n):
            self.p.append([])
            for j in range((2*self.n*self.m)+1): #
                self.p[i].append([[] for _ in range(len_v)])
        return(self.p)


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
g = generiraj_G([4, 3], 0.5)
B = BCS(g)
print(B.n)