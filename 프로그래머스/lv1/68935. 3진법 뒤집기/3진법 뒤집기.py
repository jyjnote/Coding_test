def solution(n):
    reversed_ternary = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        reversed_ternary += str(remainder)

    decimal_result = int(reversed_ternary, 3)

    return decimal_result