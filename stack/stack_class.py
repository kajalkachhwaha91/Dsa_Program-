class Stack:
  
  def __init__(self):
    self.stack = []
    
  def push(self, element):
    self.stack.append(element)
	
  def pop(self):
    if self.is_emp():
      print("stack is empty")
    else:
      self.stack.pop()
		
  def peek(self):
    if self.is_emp():
	  print("stack is empty")
    else:
      print(self.stack[-1] )
		
  def lengt(self):
    if self.is_emp():
      print("stack is empty")
    else:
      print(len(self.stack))
	
  def is_emp(self):
    return len(self.stack) == 0
		
		
my_stack = Stack()

my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print("values of stack", my_stack)

my_stack.pop()
print("values of stack", my_stack)


# my_stack.peek()

my_stack.lengt()

my_stack.is_emp()
