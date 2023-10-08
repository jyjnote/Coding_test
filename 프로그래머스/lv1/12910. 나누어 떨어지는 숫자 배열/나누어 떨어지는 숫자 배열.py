def solution(a, divisor):
    answer=[]
    for i in a:
        if i%divisor==0:
            answer.append(i)
    answer=sorted(answer)
    if not answer:
        answer.append(-1)
    return answer