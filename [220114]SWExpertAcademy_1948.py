for t in range(int(input())) :
    a_month, a_day, b_month, b_day = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(f'#{t+1} {sum(days[a_month-1:b_month-1]) + b_day - a_day+1}')