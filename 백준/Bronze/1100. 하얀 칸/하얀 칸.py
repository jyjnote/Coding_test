c = 0

b = [input() for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and b[i][j] == 'F':
            c += 1

print(c)