#similar with reverse, but add some limit
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


def reverse_every_k_elements(head, k):
    pre =None
    return reverseLIST(pre,head,k)
    
def reverseLIST(pre,head,k):
    pre = pre
    count =0
    while count<k and head!=None:
        next = head.next
        head.next =pre
        pre = head
        head = next
    if head == None:
        return pre
    else:
        return reverseLIST(head,next,k)