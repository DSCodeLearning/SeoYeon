'''
실행시간 조절때문에 출력을 한 번에 해야하네..
'''

result = []
for t in range(int(input())) :
    a, b, c, d = map(int, input().split())

    if b < c or d < a : result.append(f'#{t+1} {0}')
    else : result.append(f'#{t+1} {min(b,d) - max(a,c)}')

print(*result, sep='\n')




