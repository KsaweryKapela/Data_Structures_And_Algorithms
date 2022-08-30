class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularLLS:
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

    def create_ssl(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return 'The CSLL has been created'

    def insert_cssl(self, node_value, location):
        if self.head is None:
            return 'The list does not exist'

        else:
            new_node = Node(node_value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node

            elif location == 1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node

            else:
                index = 0
                temp_node = self.head
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
            return 'The node has been successfully inserted'

    def traverse_cssl(self,):
        if self.head is None:
            return 'The list does not exist'
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break

    def search_in_cssl(self, searched_value):
        if self.head is None:
            return 'The list does not exist'
        else:
            node = self.head
            while node:
                if searched_value == node.value:
                    return node.value
                node = node.next
                if node == self.tail.next:
                    return 'The value is not in list'

    def delete_node(self, location):
        if self.head is None:
            return 'The list does not exist'

        if location == 0:
            if self.tail == self.head:
                self.head.next = None
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next
                self.tail.next = self.head

        elif location == 1:
            if self.tail == self.head:
                self.head.next = None
                self.head = None
                self.tail = None

            else:
                node = self.head
                while node:
                    if node.next == self.tail:
                        break
                    node = node.next

                node.next = self.head
                self.tail = node

        else:
            node = self.head
            index = 0
            while index < location - 1:
                node = node.next
                index += 1
            next_node = node.next
            node.next = next_node.next

    def delete_csll(self):
        self.tail.next = None
        self.head = None
        self.tail = None


circular_SLL = CircularLLS()
print(circular_SLL.create_ssl(1))  # O(1)
#
circular_SLL.insert_cssl(0, 0)
circular_SLL.insert_cssl(2, 0)
circular_SLL.insert_cssl(2, 1)
circular_SLL.insert_cssl(2, 1)
circular_SLL.insert_cssl(10, 0)

print([node.value for node in circular_SLL])

circular_SLL.traverse_cssl()
print(circular_SLL.search_in_cssl(30))

print([node.value for node in circular_SLL])

circular_SLL.delete_node(0)  # O(n)

print([node.value for node in circular_SLL])

circular_SLL.delete_csll()

print([node.value for node in circular_SLL])
