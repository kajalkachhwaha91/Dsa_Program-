lst = [10, 20, 30, 50, 70, 50, 40, 20]

# largest = second = float('-inf')

largest= lst[0]
second= lst[0]

# for num in lst:
#   if num > largest:
#     largest = num
#   elif num > second and num != largest:
#     second = num
# print("second largest", second)
  
for i in range(len(lst)):
  if lst[i] > largest:
    second = largest
    largest = lst[i]
	  # print("1st largest value", largest)
  
  elif lst[i] > second and lst[i] != largest:
    second = lst[i]
	
print("2st largest value", second)
  