from linked_list_class import LinkedList


def remove_dup(linked_list):
    new_node = linked_list.head
    checked_numbers = {new_node.value}

    while new_node.next:

        if new_node.next.value in checked_numbers:
            new_node.next = new_node.next.next

        else:
            checked_numbers.add(new_node.next.value)
            new_node = new_node.next
    return linked_list


def remove_dup2(linked_list):
    if linked_list.head is None:
        return

    current_node = linked_list.head
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next
    return linked_list


ll = LinkedList()
ll.generate(10, 0, 5)
print(ll)

remove_dup2(ll)
print(ll)

