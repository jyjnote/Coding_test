numbers = []
for i in range(9):
    numbers.append(list(map(int, input().split())))

max_value = 0
row = 0
col = 0

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if max_value < numbers[i][j]:
            max_value = numbers[i][j]
            row = i
            col = j

print(max_value)
print(row + 1, col + 1)
