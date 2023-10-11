a, b = map(int, input().split())
a -= 1
b -= 1
r=abs(a // 4 - b // 4) + abs(a % 4 - b % 4)
print(r)