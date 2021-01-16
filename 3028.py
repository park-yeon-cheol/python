a=input()
ball=1
for i in range(0,len(a)):
    if a[i]=='A':
        if ball==1:
            ball=2
        elif ball==2:
            ball=1
    elif a[i]=='B':
        if ball==2:
            ball=3
        elif ball==3:
            ball=2
    elif a[i]=='C':
        if ball==1:
            ball=3
        elif ball==3:
            ball=1
print(ball)

#처음에 공이 1번 컵에 있으니 ball을 1로 만들고
#A,B,C에 해당하는 컵 섞기와 그때의 공 번호를 비교해주면 된다.