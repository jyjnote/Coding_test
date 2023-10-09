t = int(input())

for _ in range(t):
    h, w, p = map(int, input().split())
    floor = p % h
    room_num = p // h + 1

    if floor == 0:
        floor = h
        room_num -= 1

    print(floor * 100 + room_num)
