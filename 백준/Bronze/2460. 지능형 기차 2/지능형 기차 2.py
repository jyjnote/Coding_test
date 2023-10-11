p=0
m=[]
for i in range(10):
    a,b=map(int,input().split())
    p-=a
    p+=b
    m.append(p)
    
print(sorted(m)[-1])