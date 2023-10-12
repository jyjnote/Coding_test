def ml(s):
    r = s[::-1]
    m = 0

    for i in range(len(s)):
        if s[i:] == r[:len(s) - i]:
            m = len(s) - i
            break

    return m

S = input().strip()
m = ml(S)
print(len(S) + len(S) - m)
