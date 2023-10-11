
t = 3

for _ in range(t):
    n = int(input())
    ts = 0
    for _ in range(n):
        ts += int(input())
    if ts == 0:
        print("0")
    elif ts > 0:
        print("+")
    else:
        print("-")
