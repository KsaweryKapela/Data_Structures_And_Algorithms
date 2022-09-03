from linked_lists.exercises.linked_list_class import LinkedList

ll = LinkedList()
ll_2 = LinkedList()
ll_2.generate(3, 0, 10)
ll.generate(3, 0, 10)
print(ll)
print(ll_2)


def sum_lls(ll1, ll2):
    ll1_sum = 0
    ll2_sum = 0

    node_1 = ll1.head
    node_2 = ll2.head
    new_ll = LinkedList()

    multiplier = 1
    while node_1 or node_2:
        ll1_sum += node_1.value * multiplier
        ll2_sum += node_2.value * multiplier
        multiplier *= 10
        node_1 = node_1.next
        node_2 = node_2.next

    ll_sum = ll2_sum + ll1_sum
    print(ll_sum)
    for x in range(len(str(ll_sum))):
        new_ll.add(ll_sum % 10)
        ll_sum //= 10
    return new_ll



print(sum_lls(ll, ll_2))