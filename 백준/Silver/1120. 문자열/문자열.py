
a,b = map(str,input().split())


sp=len(a)
lis=[]
for i in range(0,len(b)+1):
    if len(b[i:i+sp])==sp:
        lis.append(b[i:i+sp])
cl=[]
for _ in range(len(lis)):
    count=0
    for i,v in zip(a,lis[_]):
        if i!=v:
            count+=1
    cl.append(count)
print(min(cl))