from linked_list_class import LinkedList


def NthToLast(linked_list, index):  # My solution... to different problem
    if linked_list.head is None:
        return

    temp_node = linked_list.head
    raw_index = 0

    while raw_index < index - 1:
        temp_node.next = temp_node.next.next
        raw_index += 1

    if index != 0:
        ll.head = ll.head.next
#
#
# ll = LinkedList()
# ll.generate(10, 0, 5)
# print(ll)
# NthToLast(ll, 2)
# print(ll)
#


def course_solution(linked_list, index):
    pointer1 = linked_list.head
    pointer2 = linked_list.head

    for i in range(index):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


ll = LinkedList()
ll.generate(10, 0, 20)
print(ll)
print(course_solution(ll, 3))
