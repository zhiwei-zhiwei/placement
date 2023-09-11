# Read the number of lines
n = int(input())

# Initialize counters for C, G, A, and T bases
c_count = 0
g_count = 0
a_count = 0
t_count = 0

# Iterate over the lines to count the bases
for _ in range(n):
    line = input()
    c_count += line.count('C')
    g_count += line.count('G')
    a_count += line.count('A')
    t_count += line.count('T')

# Compute the C-G ratio
cg_ratio = 100 * (c_count + g_count) / (a_count + t_count + c_count + g_count)

# Print the result
print(cg_ratio)
