def hiking_path(n, m, x, y, elevation_map):
    total_elevation_change = 0

    # Continue until the last column
    while y < m - 1:
        # Up, straight, and down elevation changes
        up_change = abs(elevation_map[x - 1][y + 1] - elevation_map[x][y]) if x > 0 else float('inf')
        straight_change = abs(elevation_map[x][y + 1] - elevation_map[x][y])
        down_change = abs(elevation_map[x + 1][y + 1] - elevation_map[x][y]) if x < n - 1 else float('inf')

        # Find the minimum change and its direction
        min_change = min(up_change, straight_change, down_change)

        if min_change == straight_change or (min_change == up_change and up_change == down_change):
            y += 1
            total_elevation_change += straight_change
        elif min_change == up_change:
            x -= 1
            y += 1
            total_elevation_change += up_change
        else:
            x += 1
            y += 1
            total_elevation_change += down_change

    return x, y, total_elevation_change


# Read the input
n, m = map(int, input().split())
x, y = map(int, input().split())
elevation_map = [list(map(int, input().split())) for _ in range(n)]
print(elevation_map)
# Get the result
x_end, y_end, total_change = hiking_path(n, m, x, y, elevation_map)

# Print the output
print(x_end, y_end, total_change)
