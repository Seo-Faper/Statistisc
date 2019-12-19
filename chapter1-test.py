import sys
n = int(sys.stdin.readline())

value = list()

maxA = 0
maxB = 0
for i in range(n):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    pos = [a,b]
    value.append(pos)
    maxA = max(a,maxA)
    maxB = max(b,maxB)

map = [[0 for col in range(maxA+1)] for row in range(maxB+1)]

for i in range(len(map)):
    for j in range(len(map[i])):
        if(i==0):
            map[i][j] = i+1
        elif j==0:
             map[i][j] = 1
        else:
            map[i][j] = map[i-1][j] + map[i][j-1]
#print(map)
for i in range(len(value)):
    print(map[value[i][0]+1][value[i][1]-1])
