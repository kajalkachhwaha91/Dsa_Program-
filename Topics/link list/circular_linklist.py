# circular linked list implementation in python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
	
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(1)

# node1.next = node2
# node2.next = node3
# node3.next = node1

# currentNode = node1
# startNode = node1
# print(" single circular linked list: ")
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.next

# while currentNode != startNode:
#   print(currentNode.data , end=" -> ")
#   currentNode = currentNode.next


# print("null")
  


	
node1 = Node(3)
node2 = Node(5)
node3 = Node(1)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node1
node1.prev = node3

print("double circular linked list: ")

currentNode = node1
startNode = node1

print("\n forward traversal: ")
print(currentNode.data, end=" -> ")
currentNode = currentNode.next
while currentNode != startNode:
  print(currentNode.data, end= " -> ")
  currentNode = currentNode.next
print("null")

currentNode = node3
startNode = node3

print("\n backward traversal: ")
print(currentNode.data, end= " -> ")
currentNode = currentNode.prev
while currentNode != startNode:
  print(currentNode.data, end =" -> ")
  currentNode = currentNode.prev
print("null")