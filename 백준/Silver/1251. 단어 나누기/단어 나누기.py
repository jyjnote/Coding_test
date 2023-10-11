w = list(input())
an = []
tmp = []

for i in range(1, len(w) - 1):
    for j in range(i + 1, len(w) ):
        a = w[:i]
        b = w[i:j]
        c = w[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)

for a in tmp:
    an.append(''.join(a))

print(sorted(an)[0])