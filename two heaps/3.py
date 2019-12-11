from heapq import *

def find(cap,pro,nums0,ini):
    minC=[]
    maxC=[]
    
    for i in range(0,len(pro)):
        heappush(minC,(cap[i],i))
    ava = ini
    for _ in range(nums0):
        while minC and minC[0][0] <=ava:
            capital,i = heappop(minC)
            heappush(maxC,(-pro[i],i))
        if not maxC:
            break
    ava+=-heappop(maxC)[0]
    return ava