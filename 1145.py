# #문제
# 다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.

# 서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.

from math import gcd
import collections
def lcm(x,y):
    return x*y // gcd(x,y)

num=[]
n=list(map(int,input().split()))
for i in range(0,4):
    for j in range(i+1,5):
        num.append(lcm(n[i],n[j]))
counter=collections.Counter(num)
mode=counter.most_common(1)
print(mode[0][0])

#처음에는 각 수들의 최소공배수를 구해서 리스트에 저장한 후 최빈값을 구하여 출력해주었지만 틀렸다고 나왔다.


n=list(map(int,input().split()))
num=min(n)
while True:
    count = 0
    for i in range(0,5):
        if num%n[i]==0:
            count+=1
    if count>2:
        print(num)
        break
    num+=1

#그래서 가장 작은 값을 구한 후 그 값을 계속 1씩 증가시키면서 5개의 수를 나눠서 나머지가 0인 것을 찾아 count를 증가시켜 주었다.
#count값이 3 이상일때 그 숫자를 출력하고 종료한다.
