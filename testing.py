from Vito_algo import *


def prikaz(n, m, p):
    G = generiraj_G(n, m, p)
    p = najvecji_p(G)
    print("G: ")
    # izpis grafa
    for j in range(len(G[0])):
        vrstica = [el[j] for el in G]
        print(" -- ".join([str(el) for el in vrstica]))
    print("Stevilo vozlisc BCS: ", p)

prikaz(3, 5, 1)







