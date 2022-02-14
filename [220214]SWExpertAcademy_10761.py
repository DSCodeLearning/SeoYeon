'''
버튼 K는 복도의 시작점에서 K미터 떨어져 있음
두 로봇은 버튼 1에서 시작
즉, 두 로봇은 복도의 시작점에서 1미터 떨어져있음.

1초마다 로봇은 양 방향 중 하나로 1미터 걷거나, 자기 위치에 있는 버튼을 누르거나, 아무것도 하지 않음
O x 오렌지가 x 버튼을 눌러야 함, B x 블루가 해당 버튼을 눌러야 함
동시에 버튼을 누를 수 X


'''

for t in range(int(input())) :
    a = input().split()
    n = int(a[0])
    del a[0]

    r, b, O, B = list(), list(), 1, 1

    for i in range(0, len(a), 2) : r.append(a[i]), b.append(a[i+1])

    while True :



