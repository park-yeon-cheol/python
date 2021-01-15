a,b,c=map(int,input().split())
if a+b==c:
    print(a,"+",b,"=",c,sep='')
elif a-b==c:
    print(a, "-", b, "=", c,sep='')
elif a*b==c:
    print(a, "*", b, "=", c,sep='')
elif a/b==c:
    print(a, "/", b, "=", c,sep='')
elif b+c==a:
    print(a,"=",b,"+",c,sep='')
elif b-c==a:
    print(a,"=",b,"-",c,sep='')
elif b*c==a:
    print(a,"=",b,"*",c,sep='')
elif b/c==a:
    print(a,"=",b,"/",c,sep='')

#+,-,*,/에 대한 경우의 수를 따져주면 된다.
#처음 문제를 풀 때는 등호가 맨 마지막에 있는 것만 생각해서
#틀렸었다. 그 후 앞에 등호가 나오는 경우까지 추가해 주었다.