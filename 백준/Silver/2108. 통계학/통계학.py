import sys
from collections import Counter

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
m = round(sum(a) / n)
d = sorted(a)[n // 2]
c = Counter(a)
f = max(c.values())
mo = [num for num, freq in c.items() if freq == f]
mo = min(mo) if len(mo) == 1 else sorted(mo)[1]
r = max(a) - min(a)

print(m)
print(d)
print(mo)
print(r)
