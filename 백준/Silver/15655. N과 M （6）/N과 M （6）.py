from itertools import combinations

a,b = map(int, input().split())
ns = sorted(map(int, input().split()))

for c in combinations(ns, b):
    print(*c)
