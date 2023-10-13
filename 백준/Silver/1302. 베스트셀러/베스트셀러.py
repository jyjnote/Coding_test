from collections import Counter

n = int(input())
a=[]
for _ in range(n):
    a.append(input())

best=max(a)

ca=Counter(a)

best=max(ca.values())
an = [key for key, count in ca.items() if count == best]
print(sorted(an)[0])