n = int(input())
g = []

for _ in range(n):
    s = input()
    t = sum(int(c) for c in s if c.isdigit())
    g.append((s, t))

sg = sorted(g, key=lambda x: (len(x[0]), x[1], x[0]))

for g in sg:
    print(g[0])
