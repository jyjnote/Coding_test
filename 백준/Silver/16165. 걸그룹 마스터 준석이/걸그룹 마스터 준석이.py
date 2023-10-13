N, M = map(int, input().split())
groups = {}
for _ in range(N):
    group_name = input()
    num_members = int(input())
    members = [input() for _ in range(num_members)]
    members.sort()
    for member in members:
        groups[member] = group_name
result = []
for _ in range(M):
    quiz_name = input().strip()
    quiz_type = int(input())
    if quiz_type == 0:
        for member, group in groups.items():
            if quiz_name == group:
                result.append(member)
    elif quiz_type == 1:
        result.append(groups.get(quiz_name))
for item in result:
    print(item)
