from collections import Counter

def find_mode(arr):
    counter = Counter(arr)
    max_frequency = max(counter.values())
    
    modes = [num for num, frequency in counter.items() if frequency == max_frequency]
    
    if len(modes) > 1:
        return -1
    else:
        return modes[0]

def solution(array):
    return find_mode(array)