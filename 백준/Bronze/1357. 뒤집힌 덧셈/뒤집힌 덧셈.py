a,b = map(str, input().split())
ar = int(a[::-1])
br = int(b[::-1])
r = ar+br
r = str(r)[::-1]

print(int(r))
