a=[1,2,3]
n=int(input())
for i in range(n):
    c,d=map(int,input().split())
    xi = a.index(c)
    yi = a.index(d)    
    a[xi],a[yi]=a[yi],a[xi]
print(a[0])