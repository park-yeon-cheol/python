#문제
#두 정수 A와 B가 주어졌을 때,
#두 정수 사이에 있는 수의 합을 구하는 프로그램을 작성하시오. 사이에 있는 수들은 A와 B도 포함한다.

import sys
a,b=map(int,sys.stdin.readline().split())
sum=0
for i in range(a,b+1):
    sum=sum+i
print(sum)

#처음에는 반복문을 통해 코드를 짜 주었다. 하지만 시간초과가 났다.

a,b=map(int,input().split())
result=sum(n for n in range(a,b+1))
print(result)

#두번째는 sum함수를 사용해서 풀었더니 for문 때문인지 역시나 시간초과였다.

n=list(map(int,input().split()))
a=min(n)
b=max(n)
result=(b*(b+1)//2)-((a-1)*(a)//2)
print(result)

#그 후 여러가지 방법을 살펴보다가 문제 이름인 시그마를 사용하기로 하였다.
#시그마는 1~n까지 더할때 n(n+1)/2이다. 즉 입력받은 수 중 큰 수가 n에 해당되기 때문에
#먼저 처리를 해 주고 원래의 시그마는 1부터기 때문에 작은 값으로 더한 값을 또 빼준다.
