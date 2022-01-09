from modelBCS import *

# Poisce vse vrednosti p_ijv

def P(G):
    B = BCS(G)
    n = B.n # st solpcev
    m = B.m # st vrsic 
    vzorec = B.VZ
    p = B.generiraj_p_ijv()
    #V = B.generiraj_V()
    for i in range(n): # za vsak stolpec
        for j in range((2 * n * m) + 1):
            for v in range(len(vzorec)):
                vz = vzorec[v] #potegnemo vzorec
                fj = j - n * m # pretvorimo
                vr_vz = B.vrednost_vzorca(vz, i)

                if i == 0:
                    if  vr_vz == fj:
                        p[i][j][v] = len(vz)
                        #V[i][j][v] = vz
                    elif fj == 0:
                        p[i][j][v] = 0
                        #V[i][j][v] = None
                    else:
                        p[i][j][v] = float('-inf')
                        #V[i][j][v] = None

                elif abs(fj) > (i + 1) * m:
                    p[i][j][v] = float('-inf')
                    #V[i][j][v] = None

                else:
                    #kandidati_vozlisc = [None]
                    if fj != 0:
                        kandidati = [float('-inf')]
                    else:
                        kandidati = [-len(vz)]    
                    for u in range(len(vzorec)):
                        if abs(fj - vr_vz) >= (i + 1)*m: # nam zagotovi da ne pademo ven
                            continue
                        else:

                            du = [set(sum(d, [])) for d in vzorec[u]] # deli u
                            vv = set(sum(sum(vzorec[v], []),[])) # množica vozlišč v
                            pogoj1 = all(any(x in vv for x in d) for d in du)
                            pogoj2 = all(any(all(any(x in c for x in e) for c in d) for e in du) for d in vzorec[v] if len(d) > 1)
                            if pogoj1 and pogoj2:
                                if vzorec[v] in [ [[[1], [3]]], [[[1], [4]]], [[[2], [4]]], [[[1, 2], [4]]], [[[1], [3, 4]]]] and fj == 0:
                                    continue
                                else:
                                    st_vozlisc = len(vz) + p[i - 1][j - vr_vz][u]
                                    kandidati.append(st_vozlisc)
                            #if ujemanje(vzorec[u], vz):
                                # if povezan(vzorec[u]): # vzamemo povezanega da ne prde do tezav pri max(pijv)
                                #kandidati_vozlisc.append([V[i-1][j - vr_vz][u], vz])
                    max_kandidat = max(kandidati)
                    indeks = kandidati.index(max_kandidat)
                    p[i][j][v] = max_kandidat
                    #V[i][j][v] = kandidati_vozlisc[indeks]
    return(p)

# poisce najvecji p_i0v
def max_BCS(G):
    B = BCS(G)
    p, V = P(G)
    r = len(p) # stolpec
    q = len(p[0]) # st. mej za razlike j
    s = len(p[0][0]) # st. vzorcev
    vzorci = B.VZ
    print(vzorci)
    st_vozlisc = []
    #sez_vozlisc = []
    j_0 = q//2 #potegnemo j=0
    for i in range(r):
        for v in range(s):
            if len(vzorci[v]):
            #if povezan(vzorci[v]):
                st_vozlisc.append(p[i][j_0][v])
                #sez_vozlisc.append(V[i][j_0][v])
    try:
        maxi = max(st_vozlisc)
        indeks = st_vozlisc.index(maxi)
        return(maxi)
    except ValueError:
        niz = "Graf G ne vsebuje nobenega uravnoteženega podgrafa"
        return(niz)

G1 = [[1, 1], [1, 1], [1, -1], [1, 1], [1, 1], [1, 1]] 
G3 = [[-1, 1, -1], [1, 1, 1], [-1, 1, -1]]
G4 = [[-1,1,1,1,1,-1],[1,1,1,1,1,1],[-1,1,1,1,1,-1],[1,1,1,1,1,1],[-1,1,-1,1,1,-1]]

#print(P(G1))

print(max_BCS(G1))