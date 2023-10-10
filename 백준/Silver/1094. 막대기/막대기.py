X = int(input())
c = 0

while X > 0:
    if X % 2 == 1:
        c += 1
    X //= 2

print(c)
