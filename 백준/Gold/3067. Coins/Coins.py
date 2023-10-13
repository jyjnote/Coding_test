c=[1,5,10,50,100,500]
t=int(input())
for i in range(t):
    n=int(input())
    coins=list(map(int,input().split()))
    w=int(input())
    
    dp = [0] * (w + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, w + 1):
            dp[i] += dp[i - coin]

    print(dp[w])