a, b = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

for i in nums:
    if b>=i:
        b+=1
    else:
        break
print(b)