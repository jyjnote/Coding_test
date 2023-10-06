def solution(numbers):
  
    digit_count = {i: 0 for i in range(10)}
    
 
    for num in numbers:
        digit_count[num] += 1
    
    result = sum(num for num, count in digit_count.items() if count == 0)
    
    return result
