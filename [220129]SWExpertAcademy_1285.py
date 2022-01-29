#다 풀었는데 알고보니 파이썬에서 지원이 안 되는 문제.. 개킹받음
for t in range(int(input())) :
    N = int(input())
    case = sorted([abs(int(i)) for i in input().split()])
    num = 0

    for i in case :
        if i == case[0] : num += 1

    print(f'#{t+1} {case[0]} {num}')