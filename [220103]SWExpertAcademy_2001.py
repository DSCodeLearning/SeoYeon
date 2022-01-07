# casenum = int(input())
# case = list(range(casenum))
# catchrange = list(range(casenum))
#
# for i in range(casenum) :
#     n, m[i] = map(int, input().split(' '))
#     case[i] = [list(map(int,input().split(' '))) for j in range(caserange)]
#
# print(case)
#
# for i in range(casenum) :
#     Max = 0
#
#     for j in range(len(case[i])) :
#         for k in range(case[i][j]) :
#             # if case[i][j][k] +
#
#             pass
#
#     print(f'#{i+1} {Max}')

for c in range(int(input())) :
    n, m = map(int, input().split(' '))
    case = [list(map(int,input().split(' '))) for k in range(n)]
    Max = 0

    for i in range(n-m+1) :
        for j in range(n-m+1) :
            temp = 0
            for x in range(m) :
                for y in range(m) :
                    temp += case[i+x][j+y]
            Max = max(temp, Max)
    print(f'#{c+1} {Max}')