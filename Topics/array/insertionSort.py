# The Insertion Sort algorithm uses one part of the array to hold the sorted values,
# and the other part of the array to hold values that are not sorted yet.Ex the cards as we place them in thier places just like that.
# It builds the final sorted array one item at a time.
# Time Complexity: O(n^2)

list = [23, 45, 7, 9, 1, 12, 34, 43, 88, 90]

n = len(list)
for i in range(1, n):
    currentIndex = i
    currentValue = list[i]
    for j in range(i - 1, -1, -1):
        if currentValue < list[j]:
            list[j + 1] = list[j]
            currentIndex = j
        else:
            break
    list[currentIndex] = currentValue
print("Sorted list is:", list)
