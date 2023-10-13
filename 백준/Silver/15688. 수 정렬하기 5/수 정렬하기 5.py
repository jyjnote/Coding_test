import sys

n = int(input())
l = [int(sys.stdin.readline()) for _ in range(n)]
l.sort()

for n in l:
    print(n)
