import random
import itertools
from itertools import combinations
import numpy

# GENERIRANJE MREŽ

mylist=[1,-1]

def grid(col, row):
	all_nodes=[]
	for x in range(col):
		for y in range(row):
			all_nodes.append([x,y, random.choice(mylist)])
	return all_nodes

# print (grid(2,3))     vrne [colpec, element v colpcu, barva R=1 M=-1]
m1 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1], [2, 0, 1], [2, 1, -1]]
m2 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1]]

# OSNOVNE FUNKCIJE

def set_partition(grid):
    a = [item[1] for item in grid]
    st_rowic = len(set(a))
    l = [i+1 for i in range(st_rowic)]
    return sum([list(map(list, combinations(l, i))) for i in range(len(l) + 1)], [])[1:]

print(set_partition(m1))   # --> particija colpca v mrezi [[], [1], [2], [1, 2]]

def rows(grid):
    a = [item[1] for item in grid]
    return len(set(a))

def col(grid):
    a = [item[0] for item in grid]
    return len(set(a))

def sum_of_colors(grid, pattern, col):
    j = 0
    for item in grid:
        if item[0] == col:
            for v in pattern:
                if item[1] == (v-1):
                    j = j+item[2]
    return j


def match(v1, v2):
    for el in v2:
        if el in v1:
            return True
    return False
    
# GLAVNA FUNKCIJA

def pji(grid):        #nam da prazen seznam ki ga bomo polnili [[[[]*st_vzorcev]* največja meja j]*st_colpcev]
    p = numpy.zeros( (col(grid)+1, 2* col(grid) * rows(grid) + 1 , len(set_partition(grid)) ) )
    return p

m2 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1]]
print (pji(m2))


def coloring(grid):
    p = pji(grid)
    cols = col(grid)
    row = rows(grid)
    patterns = set_partition(grid)
    for i in range(cols + 1):
        for j in range(-cols * row, cols * row + 1):
            for k in range(len(patterns)):
                if i == 0:
                    if j == 0:
                        p[i][j+cols * row][k] = 0
                    else:
                        p[i][j+cols * row][k] = float("-Inf")
                else:
                    if abs(j) > i * row:
                        p[i][j+cols * row][k] = float("-Inf")
                    else:
                        sumasion = j + sum_of_colors(grid, patterns[k] ,i) 
                        array_of_matching_elements = numpy.array([])
                        for v in patterns:
                            if match(v, patterns[k]):
                                array_of_matching_elements = numpy.append(array_of_matching_elements,[ p[i-1][j+sumasion][v] ])
                        if array_of_matching_elements == numpy.empty(0):
                            p[i][j+cols * row][k] = 0
                        else:
                            try:
                                max_value = numpy.ndarray.max(array_of_matching_elements)
                                if max_value == float("-Inf"):
                                    if j != sum_of_colors(grid, patterns[k] ,i) :
                                        p[i][j+cols * row][k] = 0
                                    else: 
                                        p[i][j+cols * row][k] = len(patterns[k])
                                else:
                                    p[i][j+cols * row][k] = max_value + len(patterns[k])
                            except ValueError:  
                                pass
    return p


print(coloring(m2))


'''
def alg(grid):
    p = pji(grid)
    col = st_colpcev(grid)
    row = st_rowic(grid)
    vzorci = pattern(grid)
    for i in range(col): 
        for j in range((2*col*row)+1): 
            for v in range(len(vzorci)):
                vzr = vzorci[v]
                if i == 0:  #postavimo vse p za prvi colpec
                    if j_vzorca(grid, vzr, i) < col*row:
                        if j_vzorca(grid, vzr, i) == -col*row + j :
                            p[0][j][v] = len(v)
                    elif j_vzorca(grid, vzr, i) >= col*row :    
                        if j_vzorca(grid, vzr, i) == j:
                            p[0][j+col*row][v] = len(v)
                    else:
                        p[i][j][v] = float(0)
                elif j > (i+1)*row+row*col or j < -(i+1)*row+row*col: #postavimo vse p kjer |j| > i|G| na -inf
                    p[i][j][v] = float(0)
                else:
                    a = [0]
                    vsota_v = j_vzorca(grid, vzr, i)
                    b = j-col*row-vsota_v
                    if b == 0:
                        a.append(len(set(vzr)))
                    for u in range(len(vzorci)):
                        vzr2 = vzorci[u]
                        if ujemanje(vzr2, vzr):
                            if b+col*row > 2*col*row+1:
                                a.append(len(set(vzr))+p[i-1][b+col*row][u])
                            else:
                                pass
                    p[i][j][v] = max(a)
    return (p)

'''

