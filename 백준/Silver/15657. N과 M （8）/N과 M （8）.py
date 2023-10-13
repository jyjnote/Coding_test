from itertools import combinations_with_replacement

a,b= map(int, input().split())
ns = sorted(map(int, input().split()))
for c in combinations_with_replacement(ns, b):
    print(*c)
