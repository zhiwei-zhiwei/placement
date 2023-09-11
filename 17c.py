# Recursive fill function
def fill(arr, i, orig_value, new_value):
    # Base cases
    if i < 0 or i >= len(arr):
        return
    if arr[i] != orig_value:
        return
    if arr[i] == new_value:
        return

    # Change the value
    arr[i] = new_value

    # Recursive calls
    fill(arr, i - 1, orig_value, new_value)  # Left
    fill(arr, i + 1, orig_value, new_value)  # Right


# Read input
n, i, new_value = map(int, input().split())
arr = list(map(int, input().split()))

# Apply the fill operation
fill(arr, i, arr[i], new_value)

# Print the result
print(' '.join(map(str, arr)))
