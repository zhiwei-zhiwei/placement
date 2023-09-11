# Read the first name and last name
first_name, last_name = input().split()

# Calculate the noble last name
if len(last_name) == 5:
    noble_last_name = last_name * 4
else:
    noble_last_name = last_name * len(last_name)

# Print the result
print(first_name + " " +noble_last_name)