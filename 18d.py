# Read number of boxes and the required volume
n, v_required = map(int, input().split())

# Initialize the maximum volume to zero
max_volume = 0

# Read each box's dimensions
for _ in range(n):
    l, w, h = map(int, input().split())
    # Calculate volume and update max_volume if it's larger
    max_volume = max(max_volume, l * w * h)

# Output the difference between max volume and the required volume
print(max_volume - v_required)
