import sys

a = int(sys.stdin.readline())
n = [0] *( 10000+1)

for _ in range(a):  # Change n to a here
    num = int(sys.stdin.readline())
    n[num] += 1

for i in range(10000+1):
    if n[i] != 0:
        for j in range(n[i]):
            print(i)
