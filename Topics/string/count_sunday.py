first_day = str(input().lower())
total_days = int(input())

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# Initialize frequency dictionary
freq = {day: 0 for day in days}

# Calculate frequencies
for i in range(total_days):
    current_day = days[(days.index(first_day) + i) % 7]
    freq[current_day] += 1

# Print the frequency of Sunday
print(freq['sunday'])