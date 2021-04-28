# #문제
# 상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다.

# 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.

# 상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

n=int(input())
a=[]
b=[]
c=[]
result=[0 for _ in range(n)]
for _ in range(0,n):
    x1,x2,x3=map(int,input().split())
    a.append(x1)
    b.append(x2)
    c.append(x3)
for j in range(0,n):
    if a.count(a[j])==1:
        result[j]+=a[j]
    if b.count(b[j])==1:
        result[j] += b[j]
    if c.count(c[j])==1:
        result[j]+=c[j]
for i in range(0,n):
    print(result[i])

