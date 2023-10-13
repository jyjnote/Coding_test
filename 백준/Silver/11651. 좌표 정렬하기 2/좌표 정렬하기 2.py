n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
sa = sorted(a, key=lambda x: (x[1], x[0]))

for p in sa:
    print(p[0], p[1])