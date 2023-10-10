def sd(num):
    ds = [int(d) for d in str(num)]
    sd = sorted(ds, reverse=True)
    return int(''.join(map(str, sd)))

num = int(input())

result = sd(num)
print(result)
