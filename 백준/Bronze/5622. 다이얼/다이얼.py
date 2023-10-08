da = {
    1: [None, 2],
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}
def calculate_dialing_time(word, dial_dict):
    time = 0
    for char in word:
        for key, value in dial_dict.items():
            if char in value:
                time += (key + 1) 
              
    return time



word = input().upper() 


total_time = calculate_dialing_time(word, da)

print(total_time)