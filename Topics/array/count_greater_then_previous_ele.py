arr = list(map(int, input().split()))
count = 1
n = len(arr)
max_so_far = arr[0]

for i in range(1, n):
    if arr[i] > max_so_far:
        count += 1
    max_so_far = max(max_so_far, arr[i])

print(count)
# import mathGiven an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.

# Note : 1st element of the array should be considered in the count of the result.
