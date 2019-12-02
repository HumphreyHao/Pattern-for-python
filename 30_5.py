class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    fast = head
    slow = head
    while fast !=slow:
        if fast == None:
            return False
        fast = fast.next
        if fast == None:
            return False
        fast = fast.next
        slow = slow.next
    return True

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))
main()