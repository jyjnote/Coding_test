n=int(input())
d=2
while n>1:
    a,b=divmod(n,d)
    if b==0:
        print(d)
        n=a
    else:
        d+=1