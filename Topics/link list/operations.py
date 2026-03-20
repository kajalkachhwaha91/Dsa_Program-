class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
	
    
def travesandprint(head):
    currentNode = head
    while currentNode:
      print( currentNode.data , end=" -> ")
      currentNode = currentNode.next
    print("null")

	
node1 = Node(3)
node2 = Node(5)
node3 = Node(1)

node1.next = node2
node2.next = node3


travesandprint(node1)



