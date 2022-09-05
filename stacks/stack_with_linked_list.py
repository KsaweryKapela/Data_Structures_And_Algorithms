class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def __str__(self):
        values = [str(item.value) for item in self.linked_list]
        return '\n'.join(values)

    def pop(self):
        if self.is_empty():
            return 'No elements'
        else:
            node_value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return node_value

    def peek(self):
        if self.is_empty():
            return 'No elements'
        node_value = self.linked_list.head.value
        return node_value

    def delete(self):
        self.linked_list.head = None


custom_stack = Stack()
custom_stack.push(1)
custom_stack.push(1)
custom_stack.push(5)
print(custom_stack)
print('---------')
print(custom_stack)
print(custom_stack.peek())

#  O(1) for all methods
