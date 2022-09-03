from linked_lists.exercises.linked_list_class import LinkedList

ll = LinkedList()
ll.generate(4, 0, 2)
ll_2 = LinkedList()
ll_2.generate(4, 0, 2)
print(f'{ll}\n{ll_2}')


def look_for_intersection(ll1, ll2):
    node = ll1.head
    node2 = ll2.head
    ll1_values = []
    intersecting_values = []

    while node:
        ll1_values.append(node.value)
        node = node.next

    while node2:
        if node2.value in ll1_values:
            del ll1_values[ll1_values.index(node2.value)]
            intersecting_values.append(node2.value)
        node2 = node2.next
    print(ll1_values)

    return intersecting_values


def look_for_intersection_2(ll1, ll2):
    node = ll1.head
    node2 = ll2.head
    intersecting_values = []

    while node:
        while node2:
            if node2.value == node.value:
                intersecting_values.append(node2.value)
                node2.value += 0.1  # To make it not take same number twice
                break
            node2 = node2.next
        node = node.next
        node2 = ll2.head

    return intersecting_values


print(look_for_intersection_2(ll, ll_2))


# COURSE SOLUTION (TO DIFFERENT PROBLEM)
# Have to analyze it more.

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

print(intersection(ll, ll_2))
