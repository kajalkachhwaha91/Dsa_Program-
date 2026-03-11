# Reasons for using linked list to implement stack:
# 1. Dynamic Size: Linked lists can grow and shrink in size dynamically, which means
#    you don't need to worry about the stack running out of space as you would with an array-based implementation.
# 2. Efficient Memory Usage: Linked lists can be more memory efficient than arrays because they
#    only allocate memory for the elements that are currently in the stack, whereas arrays may allocate more memory than needed.
# 3. Faster Insertions and Deletions: In a linked list, inserting and deleting elements is generally faster than in an array
#    because you don't need to shift elements around as you would in an array-based implementation.


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
	
class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
	
  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1
	
	
lst = Stack()
lst.push("A")
lst.push("B")
lst.push("C")
lst.push("D")
print("stack values are", Stack)
	  