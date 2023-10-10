import sys

s = []
p = s.append
o = lambda: len(s) and s.pop() or -1
i = len
e = lambda: i(s) < 1
t = lambda: e() and -1 or s[i(s) - 1]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        p(int(c[1]))
    elif c[0] == 'pop':
        print(o())
    elif c[0] == 'size':
        print(i(s))
    elif c[0] == 'empty':
        print(int(e()))
    elif c[0] == 'top':
        print(t())





