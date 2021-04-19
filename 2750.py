#문제
#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n=int(input())
result=[]
for _ in range(n):
    a=int(input())
    result.append(a)
result.sort()
for i in range(0,n):
    print(result[i],end='\n')
