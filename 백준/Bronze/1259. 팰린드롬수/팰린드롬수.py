while True:
    user_input = int(input())
    compare=str(user_input)[::-1]
    if user_input == 0:
         break
    if user_input==int(compare):
        print('yes')
    elif user_input!=int(compare):
        print('no')