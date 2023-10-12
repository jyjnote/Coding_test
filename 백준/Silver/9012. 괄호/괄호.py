def p(s):
    ss = []
    for c in s:
        if c == '(':
            ss.append(c)
        elif c == ')':
            if not ss:
                return "NO"
            ss.pop()

    return "YES" if len(ss) == 0 else "NO"
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    r = p(s)
    print(r)
