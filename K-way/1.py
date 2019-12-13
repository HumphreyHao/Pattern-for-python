from heapq import *
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

  # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value

def merge_lists(Lists):
    minHeap=[]
    for root in Lists:
        if root is not None:
            heappush(minHeap,root)
    resHead=None
    resTail=None
    while minHeap:
        node = heappop(minHeap)
        if resHead ==None:
            resHead=resTail=node
        else:
            resTail.next=node
            resTail=resTail.next
        if node.next!=None:
            heappush(minHeap,node.next)
    return resHead