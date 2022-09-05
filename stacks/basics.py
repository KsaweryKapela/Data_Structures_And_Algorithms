# Last in/ first out manner

# Stack: using list - easy to implement, but can cause speed problems
#        using linked list - hard implementation, but good performance

# Use cases:
#          LIFO functionality (last in first out)
#          The chance of data corruption is minimum
#          We can only access last element. To access first, we need to delete everyone.

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(item) for item in values]
        return '\n'.join(values)

    def is_empty(self):
        if not self.list:
            return True
        return False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if not self.list:
            return 'No element'
        else:
            return self.list.pop()

    def peek(self):
        if not self.list:
            return 'No element'
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        if not self.list:
            return True
        else:
            return False


custom_stack = Stack()
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(10)
print(custom_stack)
print(custom_stack.peek())
