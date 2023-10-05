
def find_next_greater(numbers):
    n = len(numbers)
    result = [-1] * n
    
    stack = []
    
    for i in range(n):
        while stack and numbers[i] > numbers[stack[-1]]:
    
            result[stack.pop()] = numbers[i]
 
        stack.append(i)
    
    return result

def solution(numbers):
    result = find_next_greater(numbers)
    return result