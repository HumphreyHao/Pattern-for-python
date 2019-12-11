from queue import *
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

        
def main():
    pq = PriorityQueue()
    pq.put(Job(3,"python"))
    pq.put(Job(2,"java"))
    pq.put(Job(1,"c"))
    res = pq.get()[1]
    res1=pq.get()[1]
main()
    