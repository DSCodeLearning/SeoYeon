'''
다 풀었는데.. 파이썬을 제출할 수가 없을 때.. 이런 쓰발..

입력하는 순서대로 1, 2, 3, ... N번
x, y, s
각 도시의 좌표(x, y) 각 도시의 군사력 s
case = [[1, 2, 3], [5, 3, 10]] 순서대로 x y s
case = {1 : [x, y, s], 2 : [x, y, s] ... }

0번 도시가 1번 도시에게 행사하는 영향력
case[0][2] / ((case[1][0] - case[0][0])**2 + (case[1][1] - case[0][1])**2))
1번 도시가 0번 도시에 행사하는 영향력이 0번 도시의 s 초과라면 0번 도시는 1번 도시에 위협 당한다

1) 만약 0번 도시가 다른 도시에게 위협 당하지 않는다면 군주제(K)
2) 만약 0번 도시가 다른 하나 이상의 도시들에 위협당하는데, 이들 중 영향력이 가장 큰 도시가 유일하면 항복하고, 그 도시의 체제를 따른다.
3) 만약 0번 도시가 다른 하나 이상의 도시들에 위협당하며, 이들 중 영향력이 가장 큰 도시가 두 개 이상이면 공화제(D)
    case = {1: [2, 5, 14], 2: [2, 3, 2], 3: [3, 2, 7], 4: [1, 1, 2], 5: [2, 1, 3]}
'''


for t in range(int(input())) :
    N = int(input())
    case = dict()
    for i in range(N) : case[i+1] = list(map(int, input().split()))
    eff = dict()
    result = dict()

    for i in range(1, N+1) :
        for j in range(1, N+1) :
            if i == j : continue
            else : eff[j] = (case[j][2] / ((case[i][0] - case[j][0])**2 + (case[i][1] - case[j][1])**2))

        if max(list(eff.values())) <= case[i][2] : result[i] = 'K'
        else :
            temp = 0
            for k in range(1, N+1) :
                if eff[k] > case[i][2] : temp += 1
            if temp >= 2 : result[i] = 'D'
            else : result[i] = int(max(eff.values()))

    print(f'#{t+1}', end=' ')
    print(*result.values(), sep=' ')

