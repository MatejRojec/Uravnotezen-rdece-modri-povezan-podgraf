from model import *


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
            print("\nGoodbay!\n")
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
            print("Random probability p in [0, 1] of generated weights")
            p = input("p = ")
            try:
                print()
                prikaz(int(n), int(m), float(p))
                print()
                input('[enter]')
                print('\nSelect action:')
                print("[enter] -- Retry")
                print("[e] -- EXIT")
                action = input(">")
            except ValueError:
                print(ValueError)
                print("Wrong input!")
                input('[enter]')
        elif action == "e":
            print("\nGoodbay!\n")
            break
        else:
            print("Wrong input!")
            input('[enter]')


if __name__ == "__main__":
    main_route()