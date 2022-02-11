'''
맞게 정답을 찾긴 헀는데..
파이썬으로 풀면 2000ms가 넘어가 버려서 파이썬 정답자는 한 명도 없네 ^^
'''

for t in range(int(input())) :
    N = int(input())
    case = [ list(map(int, input().split())) for i in range(N) ]
    result = 0

    for i in range(N) :
        d = (case[i][0] ** 2 + case[i][1] ** 2)**(1/2)

        if 0 <= d <= 20 : result += 10
        elif 20 < d <= 40 : result += 9
        elif 40 < d <= 60: result += 8
        elif 60 < d <= 80: result += 7
        elif 80 < d <= 100: result += 6
        elif 100 < d <= 120: result += 5
        elif 120 < d <= 140: result += 4
        elif 140 < d <= 160: result += 3
        elif 160 < d <= 180: result += 2
        elif 180 < d <= 200: result += 1
        else : result += 0

    print(f'#{t+1} {result}')