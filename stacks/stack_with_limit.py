class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(item) for item in values]
        return '\n'.join(values)

    def is_empty(self):
        if not self.list:
            return True
        return False

    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        return False

    def push(self, value):
        if self.is_full():
            return 'Stack is full'
        else:
            self.list.append(value)

    def pop(self):
        if self.is_empty():
            return 'no elements'
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            return 'no elements'
        return self.list[len(self.list)-1]


custom_stack = Stack(10)
print(custom_stack.is_full())
print(custom_stack.is_empty())
custom_stack.push(10)
custom_stack.push(12)
custom_stack.push(42)
print(custom_stack)
print(custom_stack.peek())