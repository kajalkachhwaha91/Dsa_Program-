# Bubble Sort Algorithm in Python
# it arrange the list item in order(lowest to higest)
# Time Complexity: O(n^2)
# Space Complexity: O(1)
list = [23,45, 7, 9, 1,12,34,43]

n = len(list)
for i in range(n-1):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
        
print("Sorted list is:", list)

# with improvemnet for optimization
# If no two elements were swapped by inner loop, then break
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
            swapped=True
    if not swapped:
        break
print("Sorted list is with imporvemnet:", list)