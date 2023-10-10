a = int(input())
b = [[int(x) for x in input().split()] for _ in range(a)]

r = len(b)
rl = []
t = 0
w = 0

for i in b:
    if i[0] > t:
        t = i[0]
    if i[1] > w:
        w = i[1]

for i in b:
    rank = 1
    if i[0] < t and i[1] < w:
        for j in b:
            if i != j and i[0] < j[0] and i[1] < j[1]:
                rank += 1
    rl.append(rank)

print(*rl)