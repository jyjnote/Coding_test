n=int(input())
a=[input() for i in range(n)]
if a==sorted(a)[::-1]:
    print('DECREASING')
elif a==sorted(a):
    print('INCREASING')
else:
     print('NEITHER')