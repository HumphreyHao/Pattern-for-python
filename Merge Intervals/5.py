#greedy
#use a room list 
from heapq import *
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __lt__(self, value):
        return self.end<value.end

def min_meeting_rooms(meetings):
    room_list=[]
    #sort the meeting by the start time
    #for each meeting ,when starting, chech all the meeting happens before end or not
    #that is to say ,get the min end of before meeting-keep a priorityqueue
    meetings.sort(key=lambda x : x.start)
    minRooms=0
    minHeap = []
    for meeting in meetings:
        #update all the cracking meeting, and for those not cracking meeting just keep the last one
        while (len(minHeap)>0 and meeting.start>=minHeap[0].end):
            heappop(minHeap)
        heappush(minHeap,meeting)
        minRooms = max(minRooms,len(minHeap))
    return minRooms

def main():
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()            
                    
            
            