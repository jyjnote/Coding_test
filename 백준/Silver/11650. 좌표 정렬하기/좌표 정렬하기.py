n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
p.sort()
for x, y in p:
    print(x, y)
