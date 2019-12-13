#the smallest must be in the kth-k+2th
#we should know the number,index,which list
#heap always contains nodes from all the lists, so just update the range of heap
from heapq import *
def find_smallest_range(lists):
    minHeap=[]
    res=[]#Mnumbers for M lists
    for i in range(len(lists)):
        heappush(minHeap,(lists[i][0],0,i))
        
    
    while minHeap:
        node = heappop(minHeap)
        res[i]=node[0]
        if node[1]+1<len(lists):
            heappush(minHeap,(lists[node[2]][node[1]+1],node[1]+1,node[2]))
        



def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()