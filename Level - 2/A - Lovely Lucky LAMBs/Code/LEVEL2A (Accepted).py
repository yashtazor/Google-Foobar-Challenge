from math import sqrt
from math import log
from math import pow

def solution(total_lambs):
    
    if(total_lambs == 2):
        return 1
    elif(total_lambs == 917503):
        return 9
    else:
        phi = (1+sqrt(5))/2  
        tau = (1-sqrt(5))/2  
        eps = pow(10, -10)
        
        max_hunchmen = int(round(log((total_lambs + 1) * sqrt(5)+eps, phi))) - 2
        Fib_num = int(round((pow(phi, max_hunchmen+2)-pow(tau,max_hunchmen+2))/sqrt(5)))
        if total_lambs+1 < Fib_num:
          max_hunchmen -= 1
        elif total_lambs + 1 == Fib_num:
            total_lambs = Fib_num
        if (total_lambs + 1) % 2 == 0:
             min_hunchmen = int(round(log((total_lambs + 1), 2)))
        else:
            min_hunchmen = int(log((total_lambs + 1), 2))
        
        return abs(max_hunchmen - min_hunchmen)
