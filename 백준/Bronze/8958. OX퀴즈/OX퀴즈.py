n=int(input())

for i in range(n):
    s=input()
    count=0
    sum=0
    for i in range(0,len(s)):
        if s[i]=='O':
            count+=1
            sum+=count
        else:
            count=0
    print(sum)