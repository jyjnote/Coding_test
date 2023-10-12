t = int(input()) 
for _ in range(t):
    n = int(input()) 
    sn = n + int(str(n)[::-1])
    if str(sn) == str(sn)[::-1]:
        print('YES')
    else:
        print('NO')
