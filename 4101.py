while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        if a>b:
            print("Yes")
        else:
            print("No")

#간단한 문제이다. while문을 통해 무한반복을 설정해 놓고,
#입력받은 값이 둘다 0일때 break를 사용하여 종료한다.
#첫 번째 수가 두 번째 수보다 크면 "Yes"를 출력하고
#그렇지 않으면 "No"를 출력한다.