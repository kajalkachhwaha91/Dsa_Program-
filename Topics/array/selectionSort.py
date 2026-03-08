# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
# It then repeats this process for the remainder of the array until the entire array is sorted.
# Time Complexity: O(n^2)

list = [23, 45, 7, 9, 1, 12, 34, 43]

n= len(list)
for i in range(n-1):
    minValue = i 
    for j in range(i+1, n):
        if list[j] < list[minValue]:
            minValue = j 
    res =list.pop(minValue)
    list.insert(i, res)

print("Sorted list is:", list)

# with improvemnet , by swapping instead of popping and inserting. It help in reducing time complexity.


for i in range(n-1):
    minValue = i 
    for j in range(i+1, n):
        if list[j] < list[minValue]:
            minValue = j 
    list[i], list[minValue] = list[minValue], list[i]

print("Sorted list with improvement:", list)