#문제
#첫째 줄에 줄의 수 N이 주어진다. 둘째 줄부터 N개의 줄에 각 줄의 내용이 주어진다. 각 줄에 있는 글자의 개수는 50글자를 넘지 않는다.

n=int(input())
for i in range(1,n+1):
    s = input()
    print('{0}. {1}'.format(i,s))