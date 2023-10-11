inp=int(input())
ns=list(map(int,input().split()))


count=0
for n in ns:
    for i in range(2,n+1):
        if n%i==0:
            if n==i:
                count+=1
            break
            
print(count)