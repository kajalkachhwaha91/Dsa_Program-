str_val = input()
L = int(input())

max_count = 0

for i in range(0, len(str_val), L):
    substring = str_val[i:i+L]
    count_a = substring.count('a')
    
    if count_a > max_count:
        max_count = count_a

print(max_count)