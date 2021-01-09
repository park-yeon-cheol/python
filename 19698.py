a,b,c,d=map(int,input().split())
result=(b//d)*(c//d)
if result>a:
    print(a)
else:
    print(result)