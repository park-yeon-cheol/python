N,m,M,T,R=map(int,input().split())
exercise=0
tmin=0
x=m
if m+T>M:
    print(-1)
else:
    while exercise<N:
        if x+T<=M:
            x=x+T
            exercise+=1
            tmin+=1
        else:
            if x-R<m:
                x=m
                tmin +=1
            else:
                x=x-R
                tmin +=1
    print(tmin)


#m+T이면 운동을 할 수 없기 때문에 -1을 출력하도록 하였다.
#x+T<=M이면 운동을 할 수 있기 때문에, exercise(운동한 시간)을 증가해 주고, 맥박을 변경하고 전체 운동 시간인 tmin을 증가시켜주었다.
#만약 운동이 아니라 휴식이 필요할 때는 두 가지 경우로 나뉘는데 맥박은 절대로 m보다 낮아지면 안되기 때문에 x-R<m이면  x=m으로 설정해 주었다.
