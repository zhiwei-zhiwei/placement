# Read input
n = int(input())
plate_appearances = list(map(int, input().split()))

# Calculate total number of bases from all hits
total_bases = sum([x for x in plate_appearances if x != -1])
print(total_bases)
# Count the number of at-bats (excluding walks)
at_bats = len([x for x in plate_appearances if x != -1])
print(at_bats)

# Compute the slugging average
slugging_avg = total_bases / at_bats

# Print the result
print(slugging_avg)
