num=1
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        if a<b:
            if b%a==0:
                print("factor")
        elif a%b==0 and a>b:
            print("multiple")
        else:
            print("neither")

#대소비교를 통해서 a<b이면 이고, b%a==0이면 약수이므로 factor을 출력하고,
#a%b==0이고 a>b이면 배수이므로 multiple을 출력한다.
#그 이외는 neither을 출력한다.