_, k = map(int, input().split())
s = list(map(int, input().split()))
s.sort(reverse=True)
c = s[k - 1]
print(c)
