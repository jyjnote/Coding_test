def solution(name,yearning,photo):
    x=[]
    ny=dict(zip(name,yearning))
    for i in range(0,len(photo)):
        total=0
        count=0
        for n in photo[i]:
            total+=ny.get(n,0)
            count+=1
            if count==len(photo[i]):
                x.append(total)
    return x