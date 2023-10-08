n = int(input())  # 회원 수 입력

members_dict = {}  # 나이를 키로 가지는 딕셔너리

# 회원 정보 입력받기
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)

    if age not in members_dict:
        members_dict[age] = []

    members_dict[age].append(name)

# 나이를 기준으로 오름차순 정렬
sorted_ages = sorted(members_dict.keys())

# 정렬된 나이에 대해 회원 이름 출력
for age in sorted_ages:
    for name in members_dict[age]:
        print(age, name)
