import random
from itertools import combinations

VZORCI = {
    1 :  [
        [[[1]]]
        ],
    2 :  [ 
        [[[1]]], 
        [[[2]]], 
        [[[1,2]]]],
    3 : [
        [[[1]]], 
        [[[2]]], 
        [[[3]]], 
        [[[1,2]]], 
        [[[1],[3]]], 
        [[[1]],[[3]]], 
        [[[2,3]]],
        [[[1,2,3]]]
    ],
    4 : [
        [[[1]]],
        [[[2]]],
        [[[3]]],
        [[[4]]],
        [[[1,2]]],
        [[[1],[3]]],
        [[[1]],[[3]]],
        [[[1],[4]]],
        [[[1]],[[4]]],
        [[[2,3]]],
        [[[2],[4]]],
        [[[2]],[[4]]],
        [[[3,4]]],
        [[[1,2,3]]],
        [[[1,2],[4]]],
        [[[1,2]],[[4]]],
        [[[1],[3,4]]],
        [[[1]],[[3,4]]],
        [[[2,3,4]]],
        [[[1,2,3,4]]]
    ]
}


class BCS:

    def __init__(self, G):
        self.G = G
        self.n = len(G) # st stolcev
        self.m = len(G[0]) # st vrstic
        self.VZ = VZORCI[self.m]
    
    def vrednost_vzorca(self, vzorec, i): #vrednost vzorca v i-tem stolcu grafa G
        # to vrne stali vzorec
        result = []
        for list1 in vzorec:
            for j in list1:
                for l in j:
                    result.append(l)
        vsota = 0        
        stolpec = self.G[i]
        for el in result:
            vsota += stolpec[el-1]
        return(vsota, len(result))
    
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

# pocisti seznam 
def precisti_sez(p, sez, zacetek, dolzina):
    if p == 0:
        return([])

    sez = str(sez)
    sez = sez.replace(" 2", "2").replace(" 3", "3").replace(" 4", "4")
    niz = ""
    for i in sez:
        if i in "[]":
            pass
        else:
            niz += i
    s = niz.split(" ")
    l = []
    for el in s:
        if el != ",":
            if el[-1] == ",":
                el = el[:-1]
            l.append(el)
    listic = []
    for el in l:
        v = el.split(",")
        s = []
        for i in v:
            s.append(int(i))
        listic.append(s)
    j = len(listic)-1
    for _ in range(zacetek-j):
        listic = [[]] + listic
    if dolzina-zacetek != 0:
        for _ in range(dolzina-zacetek):
            listic.append([] )
    return(listic)