from itertools import combinations_with_replacement

a,b= map(int, input().split())
cs = sorted(combinations_with_replacement(range(1, a+1), b))

for c in cs:
    print(*c)
