n = int(input())

def counts(n):
    count = 0
    while n > 0:
        n //= 5  
        count += n
    return count

zeros_count = counts(n)
print(zeros_count)
