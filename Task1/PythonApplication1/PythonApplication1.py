import math
N = 0
M = 0
H = 0
Sr = []
with open('input.txt') as in_file:
    Sr = in_file.read().split('\n')
if int(Sr[0])>= 1 and int(Sr[0]) <= int(Sr[2]) and int(Sr[2]) <= 100 and int(Sr[1])>= 1 and int(Sr[1]) <= 100:
    N = int(Sr[0])
    H = int(Sr[2])
    M = int(Sr[1])
    kol = H // N
    der = math.ceil(M / kol)
    out_file = open('output.txt', 'w')
    out_file.write(str(der))
else:
    print("Данные не удовлетворяют требованиям")

