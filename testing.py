from izpis_grafa import *


def prikaz(n, m, p):
    G = generiraj_G(n, m, p)
    p = najvecji_p(G)[0]
    print("G: ")
    # izpis grafa
    for j in range(len(G[0])):
        vrstica = [el[j] for el in G]
        print(" -- ".join([str(el) for el in vrstica]))
    print("Stevilo vozlisc BCS: ", p)
    print('BCS podgraf: ', najvecji_p(G)[1])

#prikaz(10, 3, 0.456)
prikaz(9, 3, 0.5)
#prikaz(12, 1, 0.7)
#prikaz(15, 4, 0.8)
#prikaz(5, 2, 0.85)
#prikaz(8, 2, 0.9)
#prikaz(3, 3, 0.976)
#prikaz(11, 2, 0.44)
#prikaz(12, 1, 0.56) 



def test1(n, m, p, i):
    a = []
    for _ in range(i):
        G = generiraj_G(n, m, p)
        pijv = najvecji_p(G)[0]
        print(pijv)
        a.append(pijv)
    return (a, sum(a)/len(a))

#print(test1(10, 3, 0.5, 20))    #za i=2 še dela za 3 pa ne več :(
