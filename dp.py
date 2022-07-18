import sys

input = sys.stdin.readlines()
n,x,y = list(map(int,input[0].split(' ')))
line = input[1].rstrip()

input_length = int(n)
memo = [[-1 for x in range(input_length)] for y in range(input_length)]

# for (i in range(2, input_length):
#     if line[i:i+3] == 'CAD':
#         memo[i][i+2] = 1

def calcMax(l, r):
    if memo[l][r] != -1:
        return memo[l][r]
    # if line[l] == 'C' and line[r-1] == 'D' and 'A' in line:
