class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create(self, node_value):
        node = Node(node_value)
        self.head = node
        self.tail = node
        node.previous = None
        node.next = None
        return 'The DLL is created'

    def insert(self, node_value, location):
        if self.head is None:
            return 'The list does not exist'

        else:
            new_node = Node(node_value)
            if location == 0:
                new_node.previous = None
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node

            elif location == 1:
                new_node.next = None
                new_node.previous = self.tail
                self.tail.next = new_node
                self.tail = new_node

            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.previous = temp_node
                new_node.next.previous = new_node
                temp_node.next = new_node

    def traverse(self):
        if self.head is None:
            return 'The list does not exist'
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    def reverse_traverse(self):
        if self.head is None:
            return 'The list does not exist'
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.previous

    def search(self, node_value):
        if self.head is None:
            return 'The list does not exist'
        temp_node = self.head
        while temp_node:
            if temp_node.value == node_value:
                return temp_node.value
            temp_node = temp_node.next
        return 'The value is not on the list'

    def delete(self, location):
        if self.head is None:
            return 'The list does not exist'
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
        else:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            temp_node.next = temp_node.next.next
            temp_node.next.previous = temp_node

    def delete_list(self):
        if self.head is None:
            return 'The list does not exist'
        else:
            temp_node = self.head
        while temp_node:
            temp_node.previous = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None
        print('DLL has been deleted')


dll = DoublyLinkedList()
dll.create(10)
dll.insert(5, 1)
dll.insert(5, 1)
dll.insert(5, 1)
dll.insert(100, 2)
print([node.value for node in dll])
dll.insert(13, 2)
print([node.value for node in dll])
dll.traverse()
print('now reverse')
dll.reverse_traverse()
print(dll.search(13))
print([node.value for node in dll])
dll.delete(4)
print([node.value for node in dll])
dll.delete_list()
print([node.value for node in dll])

