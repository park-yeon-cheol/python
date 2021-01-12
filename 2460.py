#2455와 똑같은 문제, 지하철 역의 수만 달라짐
import sys
sum=0
arr=[]
for i in range(0,10):
    a,b=map(int,input().split())
    sum=sum+(b-a)
    arr.append(sum)
print(max(arr))
#a,b로 입력을 받고, sum이라는 변수에 b(탄 사람)-a(내린사람) 을 해주고
#탄 지하철에 남은 사람들은 그대로 있으니 sum을 더한다.
#arr이라는 배열에 넣고, max(arr)을 통해 가장 큰 값을 출력한다.
