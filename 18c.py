def collatz_sum(n):
    # Base case: If n is 1, return 1.
    if n == 1:
        return 1

    # If n is even, add n to collatz_sum(n//2)
    elif n % 2 == 0:
        return n + collatz_sum(n // 2)

    # If n is odd, add n to collatz_sum(3*n + 1)
    else:
        return n + collatz_sum(3 * n + 1)


# Input and output
n = int(input())
print(collatz_sum(n))
