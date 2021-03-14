# #문제
# 두 정수 a와 b 최소공배수는 두 수의 공통된 배수 중 가장 작은 수이고, 최대공약수는 두 수의 공통된 약수중 가장 큰 수이다.

# a와 b가 주어졌을 때, 최소공배수와 최대공약수를 구하는 프로그램을 작성하시오.


from math import gcd
def lcm(x,y):
    result=(x*y)// gcd(x,y)
    return result

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(lcm(a,b), gcd(a,b))

    