from collections import deque

queue = deque(['one', 'two', 'three'])
queue.append('four')
queue.append('five')

print(queue)

queue.appendleft('Minus One')

print(queue)

print(queue.pop())
print(queue.popleft())