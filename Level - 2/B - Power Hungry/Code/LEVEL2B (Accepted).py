xs = [] #Enter your test list here!
    
neg = []
pos = []
zer = []
    
prod = 1
    
xs.sort()
    
for i in xs:
    if(i<0):
        neg.append(i)
    elif(i>0):
        pos.append(i)
    else:
        zer.append(i)
    
if(len(zer) == len(xs)): #All zeros.
    print(str(0))
elif(len(pos)==0 and len(neg)%2!=0 and len(zer)>0): #Zeros & odd number of negatives.
    print(str(0))
elif(len(neg)==1): #Special case, only one negative.
    print(str(neg[0]))
else: #General case.
    if(len(neg)%2 != 0):
        neg.pop()
    
    for i in neg:
        prod *= i
    
    for i in pos:
        prod *= i
    
    print(str(prod))
