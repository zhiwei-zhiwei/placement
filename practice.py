def R(s):
    if len(s) <= 1:
        return s
    return s[-1] + R(s[:-1])
in_str = input().strip()
print(R(in_str))
