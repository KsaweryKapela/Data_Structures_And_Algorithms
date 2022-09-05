from linked_lists.exercises.linked_list_class import LinkedList

ll1 = LinkedList()
ll1.generate(5, 0, 10)
print(ll1)


def get_node(node, index):
    for i in range(index):
        node = node.next
    return node


def reverse(ll):
    node = ll.head
    reversed_ll = LinkedList()

    for i in range(len(ll)):
        last_value = get_node(ll.head, len(ll) - i - 1)
        node = node.next

        reversed_ll.add(last_value)
    return reversed_ll


print(reverse(ll1))
