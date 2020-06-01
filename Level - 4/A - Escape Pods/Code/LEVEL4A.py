def solution(entrances, exits, path):
    
    a = len(entrances)
    b = len(path)
    c = len(exits)
    
    ans = 0
    
    ip = path[a:(b-c)]
    
    for i in range(len(ip)):
        sum_range = sum(ip[i])
        sum_enter = 0
        for j in entrances:
            sum_enter += path[j][a + i]
        ans += min(sum_enter, sum_range)
        
    return (ans)
