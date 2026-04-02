arr = list(map(int, input().split()))

# arr.reverse()
reverse = []

# for i in range(len(arr)-1,-1,-1):
#   reverse.append(arr[i])

# print(reverse)


# dsa approach with swapping method

start = 0
end = len(arr) - 1

while start < end:
  arr[start], arr[end] = arr[end], arr[start]
  start += 1
  end -= 1
print(arr)