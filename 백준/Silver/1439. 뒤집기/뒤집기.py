s = input().rstrip()

c = 0
d = s[0]

for i in range(1, len(s)):
    if s[i] != d:
        c += 1
        d = s[i]

print((c+1)//2)
