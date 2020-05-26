l = [-5, 0, 0]
max = -9999
prod = 1

print(l)

for i in range(0, len(l)-1):
    for j in range(i+1, len(l)):
        if(abs(l[i]) >= abs(l[j])):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)

for i in range(len(l)-1, -1, -1):
    prod *= l[i]
    if(prod > max):
        max = prod

print(str(max))
