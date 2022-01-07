'''
def GetGrade(score, N, K) :
    value = sorted(list(score.values()))

    if score[K] in value[:N // 10] : return 'D0'
    elif score[K] in value[:N // 10 * 2]: return 'C-'
    elif score[K] in value[:N // 10 * 3]: return 'C0'
    elif score[K] in value[:N // 10 * 4]: return 'C+'
    elif score[K] in value[:N // 10 * 5]: return 'B-'
    elif score[K] in value[:N // 10 * 6]: return 'B0'
    elif score[K] in value[:N // 10 * 7]: return 'B+'
    elif score[K] in value[:N // 10 * 8]: return 'A-'
    elif score[K] in value[:N // 10 * 9]: return 'A0'
    else : return 'A+'

for t in range(int(input())) :
    N, K = map(int, input().split())
    case = [list(map(int, input().split())) for i in range(N)]
    score = { i+1 : (case[i][0]*0.35 + case[i][1]*0.45 + case[i][2]*0.2) for i in range(N)}

    print(f'#{t+1} {GetGrade(score, N, K)}')
'''

#최종(다른 사람 거 베낀 거)
rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(int(input())) :
    N, K = map(int, input().split())
    case = [list(map(int, input().split())) for i in range(N)]
    score = [case[i][0]*0.35 + case[i][1]*0.45 + case[i][2]*0.2 for i in range(N)]

    student = score[K-1]
    score = sorted(score, reverse=True)
    print(f'#{t+1} {rank[score.index(student) // (N//10)]}')