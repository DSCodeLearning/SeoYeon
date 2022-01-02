casenum = int(input())
case = [input() for i in range(casenum)]

for i in range(casenum) :
    for j in range(1, 10) :
        if case[i][:j] == case[i][j:j+j] :
            print(f'#{i+1} {j}')
            break