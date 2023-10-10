n = int(input())

m = []
for _ in range(n):
    a, b = input().split()
    m.append((int(a), b))

m.sort(key=lambda x: (x[0]))

for a in m:
    print(a[0],a[1])
