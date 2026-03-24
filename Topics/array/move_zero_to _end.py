# arr = [ 2, 4, 0, 7, 8,0, 4, 0, 2]
# pos = 0

# for i in range (len(arr)):
#   if arr[i] != 0:
#     arr[pos] = arr[i]
#     pos+=1
	
# for i in range(pos, len(arr)):
#   arr[i] = 0
	
	
# print(arr)



# advance 
arr = [ 2, 4, 0, 7, 8,0, 4, 0, 2]
pos = 0

for i in range (len(arr)):
  if arr[i] != 0:
    arr[pos], arr[i] = arr[i], arr[pos]
    pos+=1
	
	
print(arr)





