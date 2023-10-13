from itertools import permutations

a,b= map(int, input().split())
numbers = list(range(1, a+1))
perms = permutations(numbers, b)

for perm in perms:
    print(' '.join(map(str, perm)))
