n=int(input())
card=[]
for i in range(1,n+1):
    card.append(i)
while True:
    if n==1:
        print(card[0])
        break
    elif n==2:
        print(card[0],card[1],end=' ')
        break
    else:
        print(card[0],end=' ')
        card.remove(card[0])
        card.append(card[0])
        card.remove(card[0])
        n-=1

#카드를 입력받고, card리스트에 숫자를 채워준다.
#첫번째 카드는 버리고 두번째 카드는 밑으로 내려야하니 remove와 append, remove를 써주어서 교통정리를 해 준다.
#n이 1인 경우에는 card[0]을 출력하고 n이 2인 경우에는 card[0],card[1]을 출력하면 된다.