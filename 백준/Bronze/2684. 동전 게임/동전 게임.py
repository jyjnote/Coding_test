d={
    'TTT': 0,
    'TTH': 0,
    'THT': 0,
    'THH': 0,
    'HTT': 0,
    'HTH': 0,
    'HHT': 0,
    'HHH': 0}

t=int(input())
for _ in range(t):
    s=input().strip()
    for i in range(0,len(s)):
        for TH,j in d.items():
            if TH in s[i:i+3]:
                d[TH]+=1
    print(*d.values())
    for TH,j in d.items():
            d[TH]=0