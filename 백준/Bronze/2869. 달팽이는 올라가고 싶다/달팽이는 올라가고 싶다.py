import math

c, m, s = map(int, input().split())

days = math.ceil((s - m) / (c - m))
print(days)