def solution(s):
    length = len(s)
    masked = '*' * (length - 4) + s[-4:]
    return masked