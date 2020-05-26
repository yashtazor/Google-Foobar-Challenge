from fractions import Fraction as f

def solution(m):
    
    idencnt = 0
    temp = []
    
    for i in range(0, len(m)): #Making P.
        denom = sum(m[i])
        if(denom == 0):
            idencnt += 1
            for j in range(0, len(m[i])):
                if(i == j):
                    m[i][j] = 1
        else:
            for j in range(0, len(m[i])):
                m[i][j] = f(m[i][j], denom)
    
    q = []
    r = []
    
    for i in range(0, len(m)-idencnt): #Finding Q
        for j in range(0, len(m)-idencnt):
            temp.append(m[i][j])
        q.append(temp)
        temp = []
    
    #print(q)
    
    temp = []
    
    for i in range(0, len(m)-idencnt): #Finding R
        for j in range(len(m)-idencnt, len(m)):
            temp.append(m[i][j])
        r.append(temp)
        temp = []
    
    #print(r)
    temp = []
    iden = []
    
    for i in range(0, len(q)): #Find I of dimensions of Q
        for j in range(0, len(q)):
            if((i+j)%2 == 0):
                temp.append(f(1, 1))
            else:
                temp.append(f(0, 1))
        iden.append(temp)
        temp = []
    
    temp = []
    ftemp = []
    
    
    
    
    for i in range(0, len(q)):
        for j in range(0, len(q)):
            temp.append(iden[i][j] - q[i][j])
        ftemp.append(temp)
        temp = []
    
    #print(ftemp) #(I-Q)
    
    
    
    
    #Inversing ftemp by Gaussian Elimination Method.
    
    for k in range(0, len(ftemp)):
        #Divide the kth row by the (k, k) element.
        x = ftemp[k][k]
    
        for i in range(0, len(ftemp)):
            ftemp[k][i] /= x
            iden[k][i] /= x
            
    
        #Alter the kth column 1 by 1.   
        
        for i in range(0, len(ftemp)):
            if(i!=k):
                x = ftemp[i][k]
                for j in range(0, len(ftemp)):
                    ftemp[i][j] -= (x*ftemp[k][j])
                    iden[i][j] -= (x*iden[k][j])
    
    #print(iden) #F matrix, i.e., (I - Q)^-1
    
    
    
    
    #Making FR.
    result = [[sum(a*b for a,b in zip(iden_row,r_col)) for r_col in zip(*r)] for iden_row in iden]
    #print(result)
    
    
    
    
    #Retreiving the final answer
    answer = []
    denom = []
    
    for i in range(0, len(result[0])):
        denom.append(result[0][i].denominator)
    
    cd = max(denom)
    
    #print(cd)
    
    for i in range(0, len(result[0])):
        x = result[0][i].denominator
        y = result[0][i].numerator
        multiplier = cd//x
        
        answer.append(y*multiplier)
    
    answer.append(cd)
    
    print(answer)

m = [
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
solution(m)
