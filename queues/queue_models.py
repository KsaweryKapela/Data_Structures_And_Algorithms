from collections import deque
import queue as q
from multiprocessing import Queue

# deque
queue = deque(maxlen=3)
print(queue)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft())
print(queue)
queue.clear()
print(queue)

# queue
queue = q.Queue(maxsize=3)
print(queue.qsize())
queue.put(1)
queue.put(1)
queue.put(1)
print(queue.qsize())
print(queue.full())
print(queue.get())
print(queue.qsize())

# multiprocessing
queue = Queue(maxsize=3)
queue.put(1)
print(queue.get())
