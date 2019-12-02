#first to find the middle
#then to reverse the second part
#compare the second and old
#reverve again
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def is_palindromic_linked_list(head):
    fast =head
    slow = head
    #find the middle
    while fast!=None and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
    #odd or even the slow.next will be the head
    second = reverse(slow)
    slow.next = second
    third =head
    while second != None and third !=None:
        if second.value == third.value:
            third =third.next
            second =second.next
        else:
            break 
    firth = reverse(slow)
    slow.next = firth
    if second !=None :
        return True
    else:
        return False
def reverse(start):
    head = start.next
    pre = None
    cur = head
    last = head.next
    while last!=None:
        tmp = last.next
        last.next = head
        head.next =pre
        pre =head
        head = last
        last =tmp
    head.next =pre
    return head
        
def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()       
