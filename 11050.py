# 문제
# 자연수 과 정수 가 주어졌을 때 이항 계수 
# 를 구하는 프로그램을 작성하시오.

from math import factorial
n,k=map(int,input().split())
result= factorial(n)//(factorial(k)*factorial(n-k))
print(result)