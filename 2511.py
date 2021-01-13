import sys
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
count_a=count_b=0
draw=0
for i in range(0,len(a)):
    if a[i]>b[i]:
        count_a=count_a+3
    elif a[i]<b[i]:
        count_b=count_b+3
    else:
        count_a=count_a+1
        count_b=count_b+1
if count_a==count_b:
    for i in reversed(range(len(a))):
        if a[i]>b[i]:
            print(count_a,count_b)
            print("A")
            break
        elif a[i]<b[i]:
            print(count_a,count_b)
            print("B")
            break
        else:
            draw=draw+1
    if draw==len(a):
        print(count_a,count_b)
        print("D")
else:
    print(count_a,count_b)
    if count_a>count_b:
        print("A")
    else:
        print("B")

#이 문제 같은 경우는 경의 수가 많다.
#A, B가 이기는 것뿐만 아니라, 비긴 경우에도 처음부터 끝까지
#모두 비기는 것이 아니면, 마지막에 누가 이겼는지도 따져 주어야 한다.
#그래서 조건문이 많다.
#또한, for 문을 사용할 때, 역순 출력을 원하면 reversed(range(n)) 이나, range(a, b, -1)의 형식으로 사용해야 한다.


