last_digits = {
    0: [0], 1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1],
    4: [4, 6], 5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1]
}

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
    else:
        cycle = last_digits[a]
        last_digit = cycle[(b - 1) % len(cycle)]
        print(last_digit)
