n = "1025"

count = 0

while(n != '1'):
    if(int(n)%2!=0):
        x = int(n)+1
        n = str(x)
        count += 1
    else:
        count += 1
        y = int(n)//2
        n = str(y)

print(count)

    
