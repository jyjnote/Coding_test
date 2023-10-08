def solution(price, money, count):
    total_cost = 0
    rides = []
    i = 1
    
    while i <= count:
        ride_cost = price * i
        rides.append(ride_cost)
        total_cost += ride_cost
        i += 1
    
    remaining_money = total_cost - money
    return max(0, remaining_money)