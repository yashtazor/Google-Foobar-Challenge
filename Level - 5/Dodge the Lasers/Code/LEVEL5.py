sqrttwo = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

sdash = lambda n: (sqrttwo*n)//(10**100) #To maintain precision. Gives s' = floor((Root(2)-1)*n)

def beatty(n): #To get the sum of Beatty sequence by recurrance formula.
    if(n == 1):
        return 1
    if(n < 1): 
        return 0
    return n*sdash(n) + ((n*(n+1))>>1) - ((sdash(n)*(sdash(n)+1))>>1) - beatty(sdash(n)) #Main formula.

def solution(n):
    return str(beatty(long(n)))
