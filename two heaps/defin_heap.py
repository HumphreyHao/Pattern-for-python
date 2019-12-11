import heapq
class Myheap(object):
    def __init__(self,initial =None, key=lambda x:x):
        super().__init__()
        self.key = key
        if initial:
            self.data =[(key(item),item)for item in initial]
            heapq.heapify(self.data)
        else:
            self.data =[]
    def push(self,item):
        heapq.heappush(self.data,(self.key(item),item))
        
    def pop(self):
        return heapq.heappop(self.data[0])
def main():
    heap = Myheap([1,2,3,4,5],key = lambda x :x[0])
    heap.push(8)
    heap.push(4)
    print(heap.pop(3))
main()
    
    