from itertools import combinations

N, t = map(int, input().split())
c = list(map(int, input().split()))

m = 0

for comb in combinations(c, 3):
    cs = sum(comb)
    if cs <= t:
        m = max(m, cs)

print(m)
