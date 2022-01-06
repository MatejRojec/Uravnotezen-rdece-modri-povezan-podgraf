import random
from itertools import combinations

#G je seznam stolpcev z utezmi (= [[stolpec 1 z utezmi], [stolpec 2 z utezmi], ...])
def generiraj_G(n, m, p): 
    # n...stevilo stolcev
    # m...stevilo vrstic
    # p...verjetnost redecega z vrednostjo 1
    vrednost = [1, -1]
    G = []
    for i in range(n):
        G.append(random.choices(vrednost, weights = [p, 1-p], k = m))
    return(G)

#print(generiraj_G(3,2, 0.5))
#G1 = [[1, -1], [-1, 1], [1, -1]]

def generiraj_vzorec(G): # generera vse mozne vzorce glede na stevilo vrstic
    n = len(G) # st stolcev
    m = len(G[0]) # st vrstic
    a = [i for i in range(1, m)]
    sez = [i+1 for i in range(m)]
    return sum([list(map(list, combinations(sez, i))) for i in range(len(sez) + 1)], [])[1:]

#print(generiraj_vzorec(G1))
# [[1], [2], [1, 2]]

def vrednost_vzorca(G, vzorec, i): #vrednost vzorca v i-tem stolcu grafa G
    vsota = 0
    stolpec = G[i]
    for el in vzorec:
        vsota += stolpec[el-1]
    return(vsota)

def ujemanje(v1, v2): #ce se vzorec v1 ujema z vzorcem v2
    for el in v2:
        if el in v1:
            return True
    return False

# nam da prazen seznam ki ga bomo polnili [ [ [ []*st_vzorcev]* največja meja j]*st_stolpcev]
def generiraj_p_ijv(G): 
    p = []
    n = len(G) # st stolpcev
    m = len(G[0]) # st vrsic 
    len_v = len(generiraj_vzorec(G))
    for i in range(n):
        p.append([])
        for j in range((2*n*m)+1): #
            p[i].append([[] for _ in range(len_v)])
    return(p)

def povezan(vzorec): # vrne ali je vzorec vzorec povezan
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


def P(G):
    n = len(G) # st stolpcev
    m = len(G[0]) # st vrsic 
    vzorec = generiraj_vzorec(G)
    p = generiraj_p_ijv(G)
    h = generiraj_p_ijv(G)
    
    for i in range(n): # za vsak stolpec
        for j in range((2*n*m) + 1):
            for v in range(len(vzorec)):
                vz = vzorec[v] #potegnemo vzorec
                fj = j - n*m # pretvorimo
                vr_vz = vrednost_vzorca(G, vz, i)

                if i == 0:
                    if  vr_vz == fj:
                        p[i][j][v] = len(vz)
                        h[i][j][v] = vz
                    else:
                        p[i][j][v] = float('-inf')
                        h[i][j][v] = None

                elif abs(fj) > (i + 1)*m:
                    p[i][j][v] = float('-inf')
                    h[i][j][v] = None

                else:
                    kandidati = [float('-inf')]
                    hji = [None]
                    for u in range(len(vzorec)):
                        if abs(fj - vr_vz) >= (i+1)*m: # nam zagotovi da ne pademo ven
                            continue
                        else:
                            if ujemanje(vzorec[u], vz):
                                if povezan(vzorec[u]): # vzamemo povezanega da ne prde do tezav pri max(pijv)
                                    st_vozlisc = len(vz) + p[i-1][j - vr_vz][u]
                                    kandidati.append(st_vozlisc)
                                    hji.append([h[i-1][j - vr_vz][u], vz])
                    p[i][j][v] = max(kandidati)
                    a = kandidati.index(max(kandidati))
                    h[i][j][v] = hji[a]
    return (p, h)

G1  = [[-1,-1,1],[-1,-1,-1], [1,-1,-1]]
# print(P(G1)[1])

def najvecji_p(G):
    p = P(G)[0]
    h = P(G)[1]
    r = len(p) # stolpec
    q = len(p[0]) # st. mej za razlike j
    s = len(p[0][0]) # st. vzorcev
    vzorci = generiraj_vzorec(G)
    st_vozlisc = []
    j_0 = q//2 #potegnemo j=0
    podgraf = []
    for i in range(r):
        for v in range(s):
            if povezan(vzorci[v]):
                if p[i][j_0][v] == float("-inf"):
                    p[i][j_0][v] = 0
                else:
                    # print(vzorci[v], p[i][j_0][v])
                    st_vozlisc.append(p[i][j_0][v])
                    podgraf.append(h[i][j_0][v])
    try:
        a = st_vozlisc.index(max(st_vozlisc))
        return(max(st_vozlisc), podgraf[a])
    except ValueError:
        niz = "Graf G ne vsebuje nobenega uravnoteženega podgrafa"
        #print("Graf G ne vsebuje nobenega uravnoteženega podgrafa")
        return(niz, niz)




G1  = [[-1,-1,-1],[-1,-1,1], [-1,-1,-1]]
print(najvecji_p(G1))

# G1 = [[1, -1], [-1, 1], [1, -1]]
# print(najvecji_p(G1))


# G2 = [[1, -1], [-1, 1], [1, -1], [1, -1]]
# print(najvecji_p(G2))
# # 8 naklucje

# G3 = [[-1, 1, -1], [1, 1, 1], [-1, 1, -1]]
# print(najvecji_p(G3))
# # 
# G4 = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1]]
# print(najvecji_p(G4))

# G5 = [[-1, -1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
# print(najvecji_p(G5))
                           
#G6 = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
# print(najvecji_p(G6))

# G7 = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
# print(najvecji_p(G7))

#G8 = [[-1, -1, -1, 1], [1, 1, -1, -1], [1, -1, 1, 1], [-1, -1, 1, 1], [-1, 1, -1, -1]]
#print(najvecji_p(G8))
# print(generiraj_vzorec(G8))

                