
class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node

    def insert(self, value, location):
        if self.head is None:
            return 'The list does not exist'
        else:
            new_node = Node(value)

            if location == 0:
                new_node.prev = self.tail
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node

            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node

            else:
                index = 0
                temp_node = self.head
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

    def traverse(self):
        if self.head is None:
            return 'The list does not exist'
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            if temp_node == self.tail:
                break
            temp_node = temp_node.next

    def reverse_traverse(self):
        if self.head is None:
            return 'The list does not exist'
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev
                if temp_node == self.head.prev:
                    break

    def search(self, value):
        if self.head is None:
            return 'The list does not exist'
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return temp_node.value
            if temp_node == self.tail:
                break
            temp_node = temp_node.next

        return 'The value is not on the list'

    def delete(self, location):
        if self.head is None:
            return 'The list does not exist'
        if location == 0:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
        elif location == 1:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
        else:
            index = 0
            temp_node = self.head
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            temp_node.next = temp_node.next.next
            temp_node.next.prev = temp_node

    def delete_list(self):
        if self.head is None:
            return 'The list does not exist'
        else:
            self.tail.next = None
            temp_node = self.head

        while temp_node:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None


cdll = CircularDLL()
cdll.create(12)
cdll.insert(32, 0)
cdll.insert(15, 1)
cdll.insert(15, 1)
cdll.insert(43, 1)
cdll.insert(43, 4)
cdll.insert(50, 1)


print([node.value for node in cdll])

cdll.traverse()
print('now reverse')
cdll.reverse_traverse()
print(cdll.search(12))
print([node.value for node in cdll])

cdll.delete(5)
print([node.value for node in cdll])

cdll.delete_list()
print([node.value for node in cdll])
