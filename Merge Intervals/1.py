class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
    #scan the timeline(my own thinking)
    #sort, and merge one by one
    if len(intervals) <2 :
        return intervals
    intervals.sort(key = lambda x : x.start)
    merged = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1,len(intervals)):
        interval = intervals[i]
        if interval.start<=end:
            end = max(end,interval.end)
        else:
            merged.append(Interval(start,end))  
            start = interval.start
            end = interval.end
    merged.append(Interval(start,end))
    return merged  
    