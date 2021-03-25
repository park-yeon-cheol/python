# #문제
# 도현이는 Counter Terror Unit (CTU)에서 일하는 특수요원이다. 도현이는 모든 사건을 정확하게 24시간이 되는 순간 해결하는 것으로 유명하다. 도현이는 1시간 만에 범인을 잡을 수 있어도 잡지 않는다. 정확하게 24시간이 되는 순간이 아니면 잡지 않는 CTU 특수요원이다.

# 2008년 3월 3일 월요일, CTU는 새학기에 맞춰 핵폭탄을 날리겠다는 테러 정보를 입수했다. CTU에서는 특수요원 도현이에게 이 임무를 맡겼다. CTU의 프로그래머 준규는 이 사건의 배후가 김선영이란 것을 해킹을 통해 밝혀내었다.

# 도현이는 선영이를 임무를 시작한지 정확하게 24시간이 되는 순간에 잡으려고 한다.

# 만약 지금 시간이 13:52:30이고, 임무를 시작한 시간이 14:00:00 이라면 도현이에게 남은시간은 00:07:30 이다.

# 모든 시간은 00:00:00 ~ 23:59:59로 표현할 수 있다. 입력과 출력에 주어지는 모든 시간은 XX:XX:XX 형태이며, 숫자가 2자리가 아닐 경우에는 0으로 채운다.

# 도현이가 임무를 시작한 시간과, 현재 시간이 주어졌을 때, 도현이에게 남은 시간을 구하는 프로그램을 작성하시오.


a=input().split(':')
b=input().split(':')
result_a=int(a[0])*3600+int(a[1])*60+int(a[2])
result_b=int(b[0])*3600+int(b[1])*60+int(b[2])
if result_a<result_b:
    result=result_b-result_a
    h=result//3600
    m=(result-(h*3600))//60
    s=(result-(h*3600))%60
    if h==0:
        print('00:',end='')
    elif h<10:
        print('0{0}:'.format(h),end='')
    else:
        print('{0}:'.format(h),end='')
    if m == 0:
        print('00:', end='')
    elif m < 10:
        print('0{0}:'.format(m), end='')
    else:
        print('{0}:'.format(m), end='')
    if s==0:
        print('00',end='')
    elif s<10:
        print('0{0}'.format(s),end='')
    else:
        print('{0}'.format(s),end='')
else:
    result=24*3600-(result_a-result_b)
    h = result // 3600
    m = (result - (h * 3600)) // 60
    s = (result - (h * 3600)) % 60
    if h == 0:
        print('00:', end='')
    elif h < 10:
        print('0{0}:'.format(h), end='')
    else:
        print('{0}:'.format(h), end='')
    if m == 0:
        print('00:', end='')
    elif m < 10:
        print('0{0}:'.format(m), end='')
    else:
        print('{0}:'.format(m), end='')
    if s == 0:
        print('00', end='')
    elif s < 10:
        print('0{0}'.format(s), end='')
    else:
        print('{0}'.format(s), end='')