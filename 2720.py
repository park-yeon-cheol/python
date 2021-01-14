t=int(input())
for i in range(0,t):
    c=int(input())
    q=c//25
    d=(c-q*25)//10
    n=(c-q*25-d*10)//5
    p=(c-q*25-d*10-n*5)
    print(q,d,n,p)

#이 문제는 큰 값부터 작은 값 순으로 계속해서 나눠주는 문제이다.
