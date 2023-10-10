d = input().strip()
w = input().strip()

c = 0
i = 0

while i < len(d):
    if d[i:i + len(w)] == w:
        c += 1
        i += len(w)
    else:
        i += 1
print(c)
