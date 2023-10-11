from collections import Counter


n= int(input())


b = list(map(int, input().split()))

card_count = Counter(b)

m = int(input())

d = list(map(int, input().split()))

for num in d:
    print(card_count[num], end=' ')