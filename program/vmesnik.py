from model import *


class barva:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"


def prikaz(n, m, p):
    G = generiraj_G(n, m, p)
    st , VZ = max_BCS(G)
    print("G:")
    #varovalo:
    if st == 0:
        for j in range(len(G[0])):
            vrstica = [vz[j] for vz in G]
            print(" -- ".join([str(el) for el in vrstica]).replace("-1", "(-)").replace("1", "(+)"))
            if j != len(G[0])-1:
                vmesna_vrstica = [" | " for _ in G]
                print("    ".join(vmesna_vrstica))
        print()
        print("Maximum size of BCS: ", st)
    else:
        # za vsak stolpec
        for i in range(len(G)):
            stolpec = ["(-)" if v == -1 else "(+)" for v in G[i]]
            for el in VZ[i]:
                if stolpec[el-1] == "(-)":
                    stolpec[el-1] = barva.RED + barva.BOLD + "(-)" + barva.ENDC
                else:
                    stolpec[el-1] = barva.BLUE + barva.BOLD + "(+)" + barva.ENDC
            G[i] = stolpec
        # za vsako vrstico
        for j in range(len(G[0])):
            vrstica = [vz[j] for vz in G]
            print(" -- ".join(vrstica))
            if j != len(G[0])-1:
                vmesna_vrstica = [" | " for _ in G]
                print("    ".join(vmesna_vrstica))
        print()
        print("Maximum size of BCS: ", st)



def main_route():
    
    while True:
        print('\nSelect action:')
        print("[c] -- Create random Grit")
        print("[e] -- EXIT")

        action = input('> ')   
        print(action)     
        if action == "c":
            main_interface_G()
            break
        elif action == "e":
            print("\nGoodbye!\n")
            break
        else:
            print("Wrong input!")
            input('[enter]')


def main_interface_G():
    
    action = ""
    while True:
        if action == "":
            print("\n-> Create Grit G size n x m, with random weights <-\n")
            print("Number of colums n")
            n = input("n = ")
            print("Number of rows m")
            m = input("m = ")
            print("Random probability p ∈ [0, 1] of generated weights")
            p = input("p = ")
            try:
                print()
                prikaz(int(n), int(m), float(p))
                print()
                input('[enter]')
                print('\nSelect action:')
                print("[enter] -- Retry")
                print("[e] -- EXIT")
                action = input("> ")
            except ValueError:
                print(ValueError)
                print("Wrong input!")
                input('[enter]')
        elif action == "e":
            print("\nGoodbye!\n")
            break
        else:
            print("Wrong input!")
            input('[enter]')
            print('\nSelect action:')
            print("[enter] -- Retry")
            print("[e] -- EXIT")
            action = input("> ")


if __name__ == "__main__":
    main_route()