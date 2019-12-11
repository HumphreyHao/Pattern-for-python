#find the first interval, whose start time is the first to bigger than end
#sort, then binary search
import bisect
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    res =[]
    intervals_3 =[]
    for i in range(len(intervals)):
        tmp=[intervals[i].start]+[intervals[i].end]+[i]
        intervals_3.append(tmp)
    intervals_3.sort(key = lambda x : x[0])
    #try to use bisect to find it
    keys=[r[0] for r in intervals_3]
    for i in intervals:
        index = bisect.bisect_left(keys,i.end)
        if index!=len(intervals_3):
            index1=intervals_3[index][2]
        else:
            index1 =-1
        res.append(index1)
    return res

def main():
    
  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()