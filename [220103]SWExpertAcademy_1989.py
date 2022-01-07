'''
1차 시도

for c in range(int(input())) :
    case = input()
    case_reverse = list(case).copy()
    case_reverse.reverse()
    temp = ''
    for i in range(len(case_reverse)) :
        temp += case_reverse[i]

    if case == temp : print(f'#{c+1} 1')
    else : print(f'#{c+1} 0')
'''

#최종
for c in range(int(input())) :
    case = input()
    if case == case[::-1] : print(f'#{c+1} 1')
    else : print(f'#{c+1} 0')