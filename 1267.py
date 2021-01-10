n=int(input())  #통화 개수
call=list(map(int,input().split())) #통화들을 list에 입력받는다.
y=m=0
for i in range(0, len(call)):   #for문으로 list에 접근하여 요금을 구한다.
    y=y+call[i]//30*10+10
    m=m+call[i]//60*15+15
if y<m:
    print("Y",y)
elif y>m:
    print("M",m)
else:
    print("Y","M",y)