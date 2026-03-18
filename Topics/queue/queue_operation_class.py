
# import queue


class Queue:
  def __init__(self):
    self.queue = []
	
  def qqueue(self, element):
    self.queue.append(element)
	
  def dequeue(self):
    if self.isEmpty():
      return "queue is empty"
    return self.queue.pop(0)
	
  def sizeque(self):
    return len(self.queue)
	
  def isEmpty(self):
    return len(self.queue) == 0
  
  def peek (self):
    if self.isEmpty():
      return " queue is empty"
    return self.queue[0]
	
ob = Queue()
ob.qqueue("k")
ob.qqueue("a")
ob.qqueue("s")
print("queue", ob.queue)


print("queue", ob.dequeue())

print("size:", ob.sizeque())

print("is empty:", ob.isEmpty())

print("peek:", ob.peek())