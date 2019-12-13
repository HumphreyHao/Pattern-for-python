class Point:
    
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dis=x*x+y*y
  def __lt__(self, other):
        return self.dis>other.dis
    #LT is less than, but it reverse,so it is a maxHeap
  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')
from heapq import *
def find_closest_points(points, k):
    minHeap=[]
    heapify(minHeap)
    for i in range(k):
        heappush(minHeap,points[i])
    #O(KlogK)
    for i in range(k,len(points)):
        if points[i]>minHeap[0]:
            heappop(minHeap)
            heappush(minHeap,points[i])
    return minHeap


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()