def calculate_end_time(start_hour, start_minute, cook_time):
    # 계산을 위해 시간과 분을 분 단위로 변환
    total_start_minutes = start_hour * 60 + start_minute
    end_time_minutes = total_start_minutes + cook_time

    # 24시간 형식으로 변환
    end_hour = end_time_minutes // 60 % 24
    end_minute = end_time_minutes % 60

    return end_hour, end_minute

# 훈제오리구이 시작 시각 입력 받기 (시, 분)
start_hour, start_minute = map(int, input().split())

# 오븐구이에 필요한 시간 입력 받기 (분)
cook_time = int(input())

# 오븐구이 끝나는 시각 계산
end_hour, end_minute = calculate_end_time(start_hour, start_minute, cook_time)

# 결과 출력
print(end_hour, end_minute)
