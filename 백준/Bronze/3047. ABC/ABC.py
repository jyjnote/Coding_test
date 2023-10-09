
A, B, C = map(int, input().split())
order = input().strip()
numbers = [A, B, C]
numbers.sort()
for char in order:
    if char == 'A':
        print(numbers[0], end=' ')
    elif char == 'B':
        print(numbers[1], end=' ')
    elif char == 'C':
        print(numbers[2], end=' ')
