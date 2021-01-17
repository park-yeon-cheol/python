n=int(input())

for i in range(0,n):
    a=int(input())
    b = []
    c=[]
    b=bin(a)[2:]
    for j in range(len(b)-1,-1,-1):
        if b[j]=='1':
            print(len(b)-j-1,end=' ')

#테스트 케이스를 n으로 입력 받고,
#리스트 b에 이진수로 변환하여 저장한다. (앞에 오는 0b는 잘라준다.)
#그 후 반복문을 사용하여 '1'을 만나면 그때의 인덱스를 출력한다.
#처음에 if문에서 if b[j]==1을 하니 출력이 되지 않았다.
#type(b[0])을 해서 확인해 보니 str타입이여서 '1'로 바꿔주었다.
