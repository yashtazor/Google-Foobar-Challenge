from fractions import Fraction as f

'''l = [[f(1, 1), f(-1, 2)], [f(-4, 9), f(1, 1)]] #2x2 Test.
iden = [[1, 0], [0, 1]]'''

'''l = [[1, 2, 6], [2, 5, 15], [6, 15, 46]] #3x3 Test.
iden = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]'''

l = [[0, -2, -3, 0], [-4, -4, -6, 0], [-7, -8, -8, -1], [0, 0, 0, 1]] #4x4 Test.
iden = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

print(l)
print(iden)

print('\n\n')

for k in range(0, len(l)):
    #Divide the kth row by the (k, k) element.
    x = l[k][k]

    if(x!=0):
        for i in range(0, len(l)):
            l[k][i] /= x
            iden[k][i] /= x
        

    #Alter the kth column 1 by 1.   
    
    for i in range(0, len(l)):
        if(i!=k):
            x = l[i][k]
            for j in range(0, len(l)):
                l[i][j] -= (x*l[k][j])
                iden[i][j] -= (x*iden[k][j])


print(l)
print(iden)
                
        
            
