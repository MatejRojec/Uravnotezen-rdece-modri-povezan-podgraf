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

# print (grid(2,3))     vrne [col, el in col.,  R=1 M=-1]
m1 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1], [2, 0, 1], [2, 1, -1]]
m2 =  [[0, 0, 1], [0, 1, 1], [1, 0, -1], [1, 1, 1]]

# OSNOVNE FUNKCIJE
def col(grid):
    a = [item[1] for item in grid]
    return len(set(a))

def rows(grid):
    a = [item[0] for item in grid]
    return len(set(a))

def set_partition(grid):
    row = rows(grid)
    l = [i+1 for i in range(row)]
    return sum([list(map(list, combinations(l, i))) for i in range(len(l) + 1)], [])[1:]

print(set_partition(m1))   # --> particija colpca v mrezi [[], [1], [2], [1, 2]]


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
    p = numpy.zeros( (col(grid)+1, 4* col(grid) * rows(grid) + 1 , len(set_partition(grid)) ) )
    return p



def coloring(grid):
    p = pji(grid)
    cols = col(grid)
    row = rows(grid)
    patterns = set_partition(grid)
    for i in range(cols + 1):
        for j in range(-2 * cols * row, 2 * cols * row + 1):
            for k in range(len(patterns)):
                if i == 0:
                    if j == 0:
                        p[i][j+ 2* cols * row][k] = 0
                    else:
                        p[i][j+ 2* cols * row][k] = float("-Inf")
                else:
                    if abs(j) > i * row:
                        p[i][j + 2* cols * row][k] = float("-Inf")
                    else:
                        sumasion = j + sum_of_colors(grid, patterns[k] ,i) 
                        array_of_matching_elements = numpy.array([])
                        for v in patterns:
                            if match(v, patterns[k]):
                                array_of_matching_elements = numpy.append(array_of_matching_elements,[ p[i-1][j+sumasion][v] ])
                        if array_of_matching_elements == numpy.empty(0) and j != sum_of_colors(grid, patterns[k] ,i):
                            p[i][j+ 2* cols * row][k] = 0
                        elif array_of_matching_elements == numpy.empty(0) and j == sum_of_colors(grid, patterns[k] ,i):
                            p[i][j+ 2* cols * row][k] = len(patterns[k])
                        else:
                            max_value = numpy.ndarray.max(array_of_matching_elements)
                            if max_value == float("-Inf"):
                                if j != sum_of_colors(grid, patterns[k] ,i) :
                                    p[i][j+ 2* cols * row][k] = 0
                                else: 
                                    p[i][j+ 2* cols * row][k] = len(patterns[k])
                            else:
                                p[i][j+ 2* cols * row][k] = max_value + len(patterns[k])
    return p

print(coloring(m1))





def alg(grid):
    p = pji(grid)
    cols = col(grid)
    row = rows(grid)
    patterns = set_partition(grid)
    for i in range(cols + 1):
        for j in range(- 2* cols * row, 2 * cols * row + 1):
            for k in range(len(patterns)):
                if i == 0:
                    if j == 0:
                        p[i][j + 2* cols * row][k] = 0
                        print(1)
                    else:
                        p[i][j + 2* cols * row][k] = float("-Inf")
                        print(2)
                else:
                    if abs(j) > i * row:
                        p[i][j + 2 * cols * row][k] = float("-Inf") 
                        print(3)
                    else:
                        sumasion = j + sum_of_colors(grid, patterns[k] ,i) 
                        array_of_matching_elements = numpy.array([])
                        print(4)
                        print(sumasion)
                        for v in patterns:
                            if match(v, patterns[k]):
                                array_of_matching_elements = numpy.append(array_of_matching_elements,[ p[i-1][j+sumasion][v] ])
                                print(5)
                        if j == 0: 
                            array_of_matching_elements = numpy.append(array_of_matching_elements,[ -len(patterns[k]) ])
                            print(6)
                        print(88)    
                        max_value = numpy.ndarray.max(array_of_matching_elements)                            
                        p[i][j+cols * row][k] = len(patterns[k]) + max_value
    return p

print(alg(m1))

