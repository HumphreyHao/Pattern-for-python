#first to find the meet N
#then use another pointer,go until they meet
#the slow1 will meet with slow2 at the meeting point
from __future__ import print_function


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    fast = head
    slow = head
    while fast!=None and fast.next!=None:
        fast =fast.next.next
        slow = slow.next
        if fast  == slow:
            break
        
    return fast
        