#timeline scan
from heapq import *
from collections import *


class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load

def find_max_cpu_load(jobs):
    #make the time line
    timeline=defaultdict(int)
    for job in jobs:
        timeline[job.start]+=job.cpu_load
        timeline[job.end]-=job.cpu_load
    mostpopular =[(x,timeline[x]) for x in timeline]
    mostpopular.sort()
    cpu_max =0
    count=0
    for i,v in mostpopular:
        count+=v
        cpu_max=max(cpu_max,count)
    return cpu_max
def main():
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
    
    
    