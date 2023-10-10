a = int(input())
b = int(input())
c = int(input())

result = a * b * c
counts = [0] * 10

while result > 0:
    counts[result % 10] += 1
    result //= 10
for count in counts:
    print(count)
