def solution(a, b):
 
    result = sum(a[i] * b[i] for i in range(len(a)))
    return result