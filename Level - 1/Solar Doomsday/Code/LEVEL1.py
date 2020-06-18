area = 15324
sum = 0
total = area
ans = []
    
while(sum != total):
    i = 1
    while((i*i) <= area):
        sq = i*i
        i = i + 1
            
    ans.append(sq)
    area = area - sq
    sum = sum + sq

ansstr = ','.join(map(str, ans)) 
print(ansstr)

