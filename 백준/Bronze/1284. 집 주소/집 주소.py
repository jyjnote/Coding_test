widths = {'0': 4, '1': 2, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3}

while True:
    number = input().strip()
    if number == '0':
        break
    total_width = sum(widths.get(digit, 3) for digit in number) + len(number) - 1 + 2
    print(total_width)
