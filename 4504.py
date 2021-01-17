n=int(input())
while True:
    a=int(input())
    if a==0:
        break
    else:
        if a%n!=0:
            print(a,"is NOT a multiple of",n,end='')
            print(".")
        else:
            print(a, "is a multiple of", n, end='')
            print(".")
#정수 n을 입력 받고, 다음 줄부터 입력받는 숫자들에 대하여
#n의 배수인지를 판별하면 되는 문제이다.