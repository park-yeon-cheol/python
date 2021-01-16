n=int(input())
a=0
b=1
c=0
if n==1:
    print(1)
else:
    for i in range(0,n):
        c=a+b
        b=a
        a=c
    print(c)

#간단한 피보나치 문제이다.
#재귀로 작성하면, 시간복잡도가 더 크기 때문에
#반복문으로 작성하였다.
#math 모듈에 factorial 구하는 것이 있었다..