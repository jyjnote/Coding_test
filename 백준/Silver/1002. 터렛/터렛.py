def calc_pos(x1, y1, r1, x2, y2, r2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if d == 0 and r1 == r2:
        return -1
    elif d == r1 + r2 or d == abs(r1 - r2):
        return 1
    elif d > r1 + r2 or d < abs(r1 - r2):
        return 0
    else:
        return 2


T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(calc_pos(x1, y1, r1, x2, y2, r2))
