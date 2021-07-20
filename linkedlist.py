class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    if head == None or head.next == None:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next= None
    return new_head

if __name__ == '__main__':

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    # Printing original linked list
    node = n1
    print("Original linked list:")
    while(node != None):
        print(node.value)
        node = node.next
    
    # Reversing linked list and printing reversed list
    node = reverse_linked_list(n1)
    print("\nReversed linked list:")
    while(node != None):
        print(node.value)
        node = node.next
