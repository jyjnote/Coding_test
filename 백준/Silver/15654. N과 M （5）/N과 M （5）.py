from itertools import permutations

a,b = map(int, input().split())
n = list(map(int, input().split()))
ps = sorted(permutations(n, b))

for p in ps:
    print(*p)
