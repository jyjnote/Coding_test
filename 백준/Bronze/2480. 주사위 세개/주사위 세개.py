def calculate_prize(dice):
    # 주어진 주사위 눈의 빈도수 계산
    dice_counts = [dice.count(i) for i in range(1, 7)]
    
    if max(dice_counts) == 3:
        return 10000 + (dice_counts.index(3) + 1) * 1000
    elif max(dice_counts) == 2:
        return 1000 + (dice_counts.index(2) + 1) * 100
    else:
        return max(dice) * 100

# 3개 주사위의 눈 입력 받기
dice = list(map(int, input().split()))

# 상금 계산
prize = calculate_prize(dice)

# 결과 출력
print(prize)
