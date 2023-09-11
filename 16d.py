def R(s):
    # Base case: if the string is empty or has only one character
    if len(s) <= 1:
        return s
    # Recursive case: take the last character and concatenate it with the reversed version of the rest of the string
    return s[-1] + R(s[:-1])

# Read the input string
input_string = input().strip()
print(input_string)
# Output the reversed string
print(R(input_string))
