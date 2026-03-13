def fact(n):
  
  if n == 1:
    return 1
	
  return n * fact(n-1)
  
print(fact(5))


def fibbo(n):

  if n == 0:
    return 0
  elif n == 1:
    return 1
  
  return fibbo(n-1) + fibbo(n-2)
  
print(fibbo(6))

def sum_num(n):
  if n == 1:
    return 1
	
  return n + sum_num(n-1)
  
print(sum_num(5))