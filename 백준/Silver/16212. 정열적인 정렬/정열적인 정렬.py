n = int(input())
l = list(map(int, input().split()))
l.sort()

for n in l:
    print(n, end=' ')
