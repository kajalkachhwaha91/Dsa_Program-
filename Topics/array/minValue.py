# iterate through an array to find the minimum value


list = [23,45, 7, 9, 1,12,34,43]
minValue = list[0]

for i in list:
    if i < minValue:
        minValue = i

print("Minimum value in the list is:", minValue)
