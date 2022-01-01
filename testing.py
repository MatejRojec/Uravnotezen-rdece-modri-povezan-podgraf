from Vito_algo import *


def prikaz(n, m, p):
    G = generiraj_G(n, m, p)
    p = najvecji_p(G)
    print("G: ")
    for j in range(len(G[0])):
        vrstica = [el[j] for el in G]
        print(" -- ".join([str(el) for el in vrstica]))
    print("Stevilo vozlisc BCS: ", p)

prikaz(1,8, 0.5)

prikaz(2, 6, 0.3)

prikaz(3, 3, 0.3)







