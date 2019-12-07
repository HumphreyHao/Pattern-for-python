#reverse alternate K
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


def reverse_alternate_k_elements(head, k):
    #KEEP THE original head
    #after the reverse,make the head point the next
    #valid the input
    if k<=1 or head == None:
          return head
    pre =None
    ori = head
    count =0
    while head !=None and count<k:
      next = head.next
      head.next = pre
      pre = head
      head = next
      count+=1
    if head == None:
      return pre
    else:
      ori.next = reverse_alternate_k_elements(next,k) 
      return pre
def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()
main()