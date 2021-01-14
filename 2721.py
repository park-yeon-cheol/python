def T(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
t=int(input())
for i in range(0,t):
    n=int(input())
    result=0
    for j in range(1,n+1):
        result=result+(j*T(j+1))
    print(result)

#이 문제는 W(n)을 구하는 문제이다.
#W(n)=Sum[k=1...n; k*T(k+1)] 이고, T(n)=1+...+n 이므로
#T(n)이라는 함수를 만들어 놓은 후, 반복문을 사용하여
#답을 구해주면 된다.