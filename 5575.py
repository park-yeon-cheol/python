# #문제
# JOI 상사는 직원의 근무시간을 타임 카드로 관리하고있다. 직원들은 전용 장비를 사용하여 타임 카드에 출근 시간을 기록한다. 근무를 마치고 퇴근할 때도 타임 카드에 퇴근 시간을 기록한다. 타임카드에서 사용하는 시간단위는 24 시간제를 사용한다.

# 보안상의 이유로 직원들의 출근 시간은 7시 이후이다. 또한, 모든 직원은 23시 이전에 퇴근한다. 직원의 퇴근 시간은 항상 출근 시간보다 늦다.

# 입력으로 JOI 상사의 3 명의 직원 A 씨, B 씨, C 씨의 출근 시간과 퇴근 시간이 주어 졌을 때 각 직원의 근무시간을 계산하는 프로그램을 작성하라.

i=0
arr=[]
while i<3:
    a,b,c,x,y,z=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    x=int(x)
    y=int(y)
    z=int(z)
    result=(x*3600+y*60+z)-(a*3600+b*60+c)
    arr.append(result//3600)
    arr.append((result%3600)//60)
    arr.append(result%60)
    i=i+1
print(arr[0],arr[1],arr[2])
print(arr[3],arr[4],arr[5])
print(arr[6],arr[7],arr[8])