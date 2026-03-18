# Basic operations of queue
queue = []

queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")

print("Queue:", queue)

deque = queue.pop(0)
print("DEQueue:", deque)

qlen =len(queue)
print("len ans size:", qlen)

peek = queue[0]
print("peek:", peek)