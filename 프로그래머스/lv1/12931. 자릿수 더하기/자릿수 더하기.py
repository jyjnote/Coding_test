def solution(n):
    answer = 0
    for i,v in enumerate(str(n)):
        answer+=int(v)
    return answer