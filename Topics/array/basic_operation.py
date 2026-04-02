lst = [10, 20, 30, 50, 70, 50, 40, 20]

for i in lst:
  print("iteration is ", i)
  
lst.append(100)
lst.append(200)
print("list after appending 100 and 200 is ", lst)

lst.remove(30)
print("list after removing 30 is ", lst)

if 50 in lst:
  print(" 50 is present in list")
  