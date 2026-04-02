lst = [10, 20, 30, 50, 70, 50, 40, 20, 100]

largest = lst[0]

# for num in lst:
#   if num > largest:
#     largest = num
# print("largest value", largest)
  

#   dsa and algo question: find the largest element in an array without using built in function
for i in range(1, len(lst)):
  if lst[i] > largest:
    largest = lst[i]
	
print("largest value", largest)

