# for t in range(int(input())) :
#     h1, m1, h2, m2 = map(int, input().split())
#     result_h = h1+h2
#     result_m = m1+m2
#
#     if result_m >= 60 :
#         temp = result_m//60
#         result_m -= temp*60
#         result_h += temp
#
#     if result_h > 12 : result_h -= 12
#
#     print(f'#{t+1} {result_h} {result_m}')

#최종(남의 것 베낌. 이런 방법도 있구나.. 난 바부였군아)
for t in range(int(input())) :
    h1, m1, h2, m2 = map(int, input().split())
    print(f'#{t+1} {(h1+h2)%12 +(m1+m2)//60 } {(m1+m2)%60}')