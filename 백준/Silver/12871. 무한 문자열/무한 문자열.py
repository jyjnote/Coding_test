def sol(s, t):
    f_s = s * len(t)
    f_t = t * len(s)
    return f_s == f_t
s = input().strip()
t = input().strip()
if sol(s, t):
    print(1)
else:
    print(0)
