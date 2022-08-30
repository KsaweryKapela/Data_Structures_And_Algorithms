class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertion(self, value, location):  # NEEDS REVISION!
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == - 1:
                new_node.next = None
                self.tail.next = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def traverse(self):
        if self.head is None:
            print('The single linked list does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def find_node(self, node_value):
        if self.head is None:
            print('The single linked list does not exist')
        else:
            node = self.head
            while node is not None:
                if node.value == node_value:
                    return node.value
                node = node.next
            return 'Value isnt on the list'

    def delete_node(self, index):
        if self.head is None:
            return 'the list does not exist'

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        elif index == 1:  # For review
            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node

        else:
            temp_node = self.head
            index_value = 0
            while index_value < index - 1:
                temp_node = temp_node.next
                index_value += 1
            next_node = temp_node.next
            temp_node.next = next_node.next

    def delete_whole_list(self):
        if self.head is None:
            return 'The list does not exist'

        self.head = None
        self.tail = None


my_linked_list = SingleLinkedList()
my_linked_list.insertion(1, 1)
my_linked_list.insertion(2, 1)
my_linked_list.insertion(3, -1)
my_linked_list.insertion(4, 1)

my_linked_list.insertion(0, 0)  # inserting 0 at the beginning O(1)
my_linked_list.insertion(0, 3)  # inserting 0 as 4th element O(n)
my_linked_list.insertion(10, -1)  # inserting 10 as last element O(1)

print([node.value for node in my_linked_list])

my_linked_list.traverse()  # O(n)
print(my_linked_list.find_node(33))  # O(n)

print([node.value for node in my_linked_list])

my_linked_list.delete_node(0)  # O(n)

print([node.value for node in my_linked_list])

my_linked_list.delete_whole_list()  # O(1)

print([node.value for node in my_linked_list])
