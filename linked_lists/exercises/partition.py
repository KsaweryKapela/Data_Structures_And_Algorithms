from linked_list_class import LinkedList

ll = LinkedList()
ll.generate(10, 0, 20)
print(ll)


def partition(linked_list, number):
    current_node = linked_list.head
    linked_list.tail = linked_list.head

    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < number:
            current_node.next = linked_list.head
            linked_list.head = current_node
        else:
            linked_list.tail.next = current_node
            linked_list.tail = current_node
        current_node = next_node

    if ll.tail.next is None:
        ll.tail.next = None


partition(ll, 5)
print(ll)
