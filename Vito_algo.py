import random
from itertools import combinations





# print(mreza(2,3))
m1 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1], [2, 0, 1], [2, 1, -1]]
m2 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1]]

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
G1 = [[1, -1], [-1, 1], [1, -1]]

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
    for v in vzorec:
        vsota += stolpec[v-1]
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


def P(G):
    n = len(G) # st stolpcev
    m = len(G[0]) # st vrsic 
    vzorec = generiraj_vzorec(G)
    p = generiraj_p_ijv(G)
    
    for i in range(n): # za vsak stolpec
        for j in range((2*n*m) + 1):
            for v in range(len(vzorec)):
                vz = vzorec[v] #potegnemo vzorec
                fj = j - n*m # pretvorimo
                vr_vz = vrednost_vzorca(G, vz, i)

                if i == 0:
                    if  vr_vz == fj:
                        p[i][j][v] = len(vz)
                    else:
                        p[i][j][v] = float('-inf')

                elif abs(fj) > (i + 1)*m:
                    p[i][j][v] = float('-inf')

                else:
                    kandidati = [float('-inf')]
                    for u in range(len(vzorec)):
                        if abs(fj - vr_vz) >= (i+1)*m: # nam zagotovi da ne pademo ven
                            continue
                        else:
                            if ujemanje(vzorec[u], vz):
                                st_vozlisc = len(vz) + p[i-1][j - vr_vz][u]
                                kandidati.append(st_vozlisc)
                    p[i][j][v] = max(kandidati)
    return(p)

def najvecji_p(G):
    p = P(G)
    r = len(p) # stolpec
    q = len(p[0]) # st. mej za razlike j
    s = len(p[0][0]) # st. vzorcev
    st_vozlisc = []
    j_0 = q//2 #potegnemo j=0
    for i in range(r):
        for v in range(s):
            if p[i][j_0][v] == float("-inf"):
                p[i][j_0][v] = 0
            else:
                st_vozlisc.append(p[i][j_0][v])
    try:
        return(max(st_vozlisc))
    except ValueError:
        print("Graf G ne vsebuje nobenega uravnoteženega podgrafa")



G1 = [[1, -1], [-1, 1], [1, -1]]
print(najvecji_p(G1))


G2 = [[1, -1], [-1, 1], [1, -1], [1, -1]]
print(najvecji_p(G2))
# 8 naklucje

G3 = [[-1, 1, -1], [1, 1, 1], [-1, 1, -1]]
print(najvecji_p(G3))
# 
G4 = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1]]
print(najvecji_p(G4))

G5 = [[-1, -1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
print(najvecji_p(G5))
                            
G6 = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
print(najvecji_p(G6))

G7 = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
print(najvecji_p(G7))


                

            

    

