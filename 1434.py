n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(sum(a)-sum(b))

#빈 박스 n개에 책m권을 넣는 문제이다.
#모든 책을 박스에 넣을 수 있는 경우로만 입력으로 주어지기 때문에
#박스의 합 - 책의 합을 하면 박스의 빈 공간이 나온다.