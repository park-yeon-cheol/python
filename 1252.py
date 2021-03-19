#문제
#두 개의 이진수를 입력받아 이를 더하는 프로그램을 작성하시오.

a,b=input().split()
a=int(a,2)
b=int(b,2)
result=a+b
print(bin(result)[2:])