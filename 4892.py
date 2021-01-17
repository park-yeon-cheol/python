num=1
while True:
    n=int(input())
    if n==0:
        break
    else:
        n1=3*n
        if n1%2==0:
            n2=n1/2
        else:
            n2=(n1+1)/2
        n3=3*n2
        n4=n3//9
        if n1%2==0:
            print(num,end='')
            print(". even",int(n4))
        else:
            print(num,end='')
            print(". odd",int(n4))
        num+=1

#게임 방식 그대로 따라한 후, n1의 홀수 짝수 구분과 n4를 구하면 된다.
#num을 지정해 주지 않아서 3번이나 틀렸다...