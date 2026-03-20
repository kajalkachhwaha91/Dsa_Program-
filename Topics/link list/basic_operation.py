# single and doubly linked list implementation in python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
	
node1 = Node(3)
node2 = Node(5)
node3 = Node(1)

node1.next = node2
node2.next = node3

currentNode = node1
while currentNode:
  print(currentNode.data, end=" -> ")
  currentNode = currentNode.next
print("null")
  


	
node1 = Node(3)
node2 = Node(5)
node3 = Node(1)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

print("Traversing forward")
currentNode = node1
while currentNode:
  print(currentNode.data, end =" -> ")
  currentNode = currentNode.next
print("null")

print("Traversing backwards")
currentNode = node3
while currentNode:
  print(currentNode.data, end =" -> ")
  currentNode = currentNode.prev
print("null")