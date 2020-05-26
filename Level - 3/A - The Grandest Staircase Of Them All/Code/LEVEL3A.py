n = # Enter test value of n.

l = [[0 for i in range(0, n+1)] for j in range(0, n+1)]

l[0][0] = 1

for i in range(1, n+1):
    for j in range(0, n+1):
        l[i][j] = l[i-1][j]

        if(j >= i):
            l[i][j] += l[i-1][j-i]

print(l[n][n]-1)
