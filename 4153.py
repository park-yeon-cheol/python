while True:
    a,b,c=list(map(int,input().split()))

    if a==0 and b==0 and c==0:
        break
    elif c==max(a,b,c):
        if c**2==a**2+b**2:
            print("right")
        else:
            print("wrong")
    elif b==max(a,b,c):
        if b**2==a**2+c**2:
            print("right")
        else:
            print("wrong")
    elif a==max(a,b,c):
        if a**2==c**2+b**2:
            print("right")
        else:
            print("wrong")

#가장 큰 수의 제곱 = 나머지 두 수의 제곱의 합으로 구해주면 된다.
