stack = []

stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushing 1, 2, 3:", stack)

top_ele = stack[-1]
print("Top element of the stack:", top_ele)

stack.pop()
print("Stack after popping the top element:", stack)

print(len(stack))

is_emp = len(stack) == 0
print("Is the stack empty?", is_emp)
