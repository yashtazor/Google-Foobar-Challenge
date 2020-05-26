n = "1025"

n = int(n)
count = 0
    
while(n > 1):
    if(n&1 == 0): #Checks if even or odd in binary. If even, devide by 2 by right shifting by one place.
        n >>= 1
    else:
        n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1) #For efficiently checking whether to increment or decrement 1, divide by 4 and then check.
                
    count += 1
    
print(count)
