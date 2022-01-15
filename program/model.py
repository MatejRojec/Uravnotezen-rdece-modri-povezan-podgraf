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
    sez = sez.replace("1], ", "1,").replace("2], ", "2,").replace("3], ", "3,")
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


def P(G):
    B = BCS(G)
    n = B.n # st solpcev
    m = B.m # st vrsic 
    vzorec = B.VZ
    p = B.generiraj_p_ijv()
    V = B.generiraj_V()
    for i in range(n): # za vsak stolpec
        for j in range((2 * n * m) + 1):
            for v in range(len(vzorec)):
                vz = vzorec[v] #potegnemo vzorec
                fj = j - n * m # pretvorimo
                vr_vz, dolzina_v = B.vrednost_vzorca(vz, i)

                if i == 0:
                    if any(len(d) > 1 for d in vzorec[v]):
                        p[i][j][v] = float('-inf')
                        V[i][j][v] = [[]]
                    else:
                        if  vr_vz == fj:
                            p[i][j][v] = dolzina_v
                            V[i][j][v] = vz
                        elif fj == 0:
                            p[i][j][v] = 0
                            V[i][j][v] = [[]]
                        else:
                            p[i][j][v] = float('-inf')
                            V[i][j][v] = [[]]

                elif abs(fj) > (i + 1) * m:
                    p[i][j][v] = float('-inf')
                    V[i][j][v] = [[]]

                else:
                    kandidati_vozlisc = [[[]]]
                    if fj != 0:
                        kandidati = [float('-inf')]
                    else:
                        kandidati = [0]    
                    for u in range(len(vzorec)):
                        if abs(fj - vr_vz) >= (i + 1)*m: # nam zagotovi da ne pademo ven
                            continue
                        else:
                            du = [set(sum(d, [])) for d in vzorec[u]] # deli u
                            vv = set(sum(sum(vzorec[v], []),[])) # množica vozlišč v
                            pogoj1 = all(any(x in vv for x in d) for d in du)
                            pogoj2 = all(any(all(any(x in c for x in e) for c in d) for e in du) for d in vzorec[v] if len(d) > 1)
                            if pogoj1 and pogoj2:
                                if any(len(d) > 1 for d in vzorec[v]) and p[i - 1][j - vr_vz][u] == 0:
                                    continue
                                else:
                                    st_vozlisc = dolzina_v + p[i - 1][j - vr_vz][u]
                                    kandidati.append(st_vozlisc)
                                    kandidati_vozlisc.append([V[i-1][j - vr_vz][u], vz])
                    max_kandidat = max(kandidati)
                    indeks = kandidati.index(max_kandidat)
                    p[i][j][v] = max_kandidat
                    V[i][j][v] = kandidati_vozlisc[indeks]
    return(p, V)


# poisce najvecji p_i0v
def max_BCS(G):
    B = BCS(G)
    p, V = P(G)
    r = len(p) # stolpec
    q = len(p[0]) # st. mej za razlike j
    s = len(p[0][0]) # st. vzorcev
    vzorci = B.VZ
    st_vozlisc = []
    sez_vozlisc = []
    j_0 = q//2 #potegnemo j=0
    l = []
    for i in range(r):
        for v in range(s):
            if len(vzorci[v]) == 1:
                st_vozlisc.append(p[i][j_0][v])
                sez_vozlisc.append(V[i][j_0][v])
                l.append(i)
    maxi = max(st_vozlisc)
    indeks = st_vozlisc.index(maxi)
    podgraf = precisti_sez(maxi, sez_vozlisc[indeks], l[indeks], B.n - 1)
    return(maxi, podgraf)
