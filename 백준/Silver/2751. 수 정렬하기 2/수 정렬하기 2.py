s = int(input())  # 입력받을 숫자의 개수
numbers = []  # 숫자를 담을 리스트

# 숫자 입력 받기
for i in range(s):
    num = int(input())
    numbers.append(num)

# 리스트를 오름차순으로 정렬
numbers.sort()

# 정렬된 숫자 출력
for num in numbers:
    print(num)
