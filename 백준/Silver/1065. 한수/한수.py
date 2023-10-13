def h(num):
    digits = [int(d) for d in str(num)]
    if len(digits) <= 2:
        return True
    diff = digits[1] - digits[0]
    return all(digits[i] - digits[i-1] == diff for i in range(2, len(digits)))
def ch(N):
    return sum(1 for num in range(1, N + 1) if h(num))

N = int(input())
print(ch(N))
