q,e = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = a + b

ca.sort()
for num in ca:
    print(num, end=' ')
