#문제
#n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n=int(input())
x=1
sum=0
while x<=n:
    sum=sum+x
    x=x + 1
print(sum)

#while문을 이용하여 풀어주었다.

a=int(input())
result=sum(n for n in range(1,a+1))
print(result)

#sum함수를 이용해서 코드 수를 더 줄일 수 있다.