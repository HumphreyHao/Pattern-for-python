#use two heap, one is the small heap, one is the large heap.
#to get the medium
from heapq import *
class MedianOfAStream:
    maxHeap = []
    #save with minus number, easy to sort,accending
    minHeap = []
    def insert_num(self, num):
        if not self.maxHeap or -self.maxHeap[0]>=num:
            heappush(self.maxHeap,-num)
        else:
            heappush(self.minHeap,num)
        
        #balance
        if len(self.maxHeap)>len(self.minHeap)+1:
            heappush(self.minHeap,-heappop(self.maxHeap[0]))
        elif len(self.maxHeap)<len(self.minHeap):
            heappush(self.maxHeap,-heappop(self.minHeap[0]))
            
    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2.0+self.minHeap[0]/2.0
        return -self.maxHeap[0]/2.0