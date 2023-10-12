a, b = map(int, input().split())

q = a // b
r = a % b
m = (q + 1) ** r * (q) ** (b - r)

print(m)
