# First in/ first out FIFO

# Implementation: python list, linked list

# Enqueue (insert) or dequeue (remove)

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return 'The element is inserted at the end of Queue'

    def dequeue(self):
        if self.is_empty():
            return 'No element in the queue'
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return 'Q is empty'
        else:
            return self.items[0]

    def delete(self):
        self.items = None


custom_queue = Queue()
print(custom_queue.is_empty())
custom_queue.enqueue(1)
custom_queue.enqueue(3)
custom_queue.enqueue(1)
print(custom_queue)
custom_queue.dequeue()
print(custom_queue)
