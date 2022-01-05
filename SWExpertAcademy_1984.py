'''
첫 번째로 시도한 방법
for c in range(int(input())) :
    case = list(input().split())
    if '' in case : case.remove('')
    case = [int(i) for i in case]
    case.sort()
    del case[0]
    del case[-1]
    print(f'#{c+1} %.0f' %(sum(case) / len(case)))
'''

#다른 방법(다른 사람의 좋은 방법)
for c in range(int(input())) :
    case = sorted(list(map(int, input().split())))[1:-1]
    print(f'#{c+1} %.0f' %(sum(case) / len(case)))
