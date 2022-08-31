class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


linked_list = SingleLinkedList()
node1 = Node(1)
node2 = Node(2)

linked_list.head = node1
linked_list.head.next = node2
linked_list.tail = node2

# O(n) time complexity for whole linked_list
# Same with space, if there's only head and tail. Else O(n)
