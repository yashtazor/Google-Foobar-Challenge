def solution(total_lambs):
    checksum = 0
        
    gen = []
    sti = []
    
    i = 0
    while(checksum < total_lambs):
        item = 2**i
        checksum = checksum + item
        if(checksum < total_lambs):
            gen.append(item)
            i += 1
        else:
            break  
    
    l1 = len(gen)
    
    sti = [1, 1]
    checksum = 0
    checker = 0
    
    while(checker < total_lambs):
        checksum = sti[-1] + sti[-2]
        checker = checker + checksum
        if(checker < total_lambs):
            sti.append(checksum)
        else:
            break

    l2 = len(sti)

    print(abs(l1-l2))


