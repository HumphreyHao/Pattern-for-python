from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverse(head):
    pre =None
    while head!=None:
        next = head.next
        head.next = pre
        pre = head
        head =next
    return pre