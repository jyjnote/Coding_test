dice = list(map(int, input().split()))

counts = [dice.count(i) for i in range(1, 7)]

if 3 in counts:
    prize = 10000 + (counts.index(3) + 1) * 1000
elif 2 in counts:
    prize = 1000 + (counts.index(2) + 1) * 100
else:
    prize = max(dice) * 100

print(prize)
