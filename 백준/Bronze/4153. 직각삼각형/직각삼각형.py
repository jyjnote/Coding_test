def t(a, b, c):
    return a**2 + b**2 == c**2

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    a, b, c = sorted([a, b, c])

    if t(a, b, c):
        print("right")
    else:
        print("wrong")
