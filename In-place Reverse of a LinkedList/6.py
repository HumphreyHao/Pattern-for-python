#find the cut point
#original cut point is in end and head
class Node:
    def __init__(self,value,next=next):
        self.value = value
        self.next =next
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
def rotate(head, rotations):
    #find the end and length
    ori =head
    count =0
    while head.next != None:
        head=head.next
        count+=1
    end = head
    end.next =ori
    length = count+1
    count =0
    #use the % remainder
    while count < rotations%length:
        ori=ori.next
        end =end.next
        count+=1
    end.next =None
    return ori
    