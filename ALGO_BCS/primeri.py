from algoritem import *

# 1 x n (pot)
G1 = [[1], [1], [1], [-1], [-1], [1], [1], [-1], [1], [1]] 
print(G1)
print(max_BCS(G1))
# 2 x n
G2 = [[1, 1], [1, 1], [1, -1], [1, 1], [1, -1], [1, 1]] 
print(G2)
print(max_BCS(G2))
# 3 x n
G3 = [[1, 1, 1], [1, 1, -1], [-1, 1, -1], [1, 1, 1]]
print(G3)
print(max_BCS(G3))
# 4 x n
G4 = [[-1,1,1,1], [1,1,1,1], [-1,1,1,1], [1,1,1,1], [-1,1,-1,1]]
print(G4)
print(max_BCS(G4))
# random graf 
rand_G = generiraj_G(8, 4, 0.2)
print(rand_G)
print(max_BCS(rand_G))

