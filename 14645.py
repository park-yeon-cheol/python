# 문제
# 버스 운전수 비와이 씨가 운전하는 버스(verse아님 ㅎ)는 N개의 정거장을 거친 후 종착역에 도착한다. 각 정거장은 내릴 인원수와 올라탈 인원수가 정해져 있다. 종착역에 도착하면 버스에 타고 있던 모든 사람이 내린다.

a,b=input().split()
a=int(a)
b=int(b)

count=0
i=0
while True:
    if count==a:
        break
    c,d=input().split()
    count=count+1

print("비와이")