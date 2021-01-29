n,k=map(int,input().split())
a=list(map(str,input().replace(',','')))
b=[]
i=0
while i<len(a):
    if a[i]=='-':
        b.append(-1*int(a[i+1]))
        i+=2
    else:
        b.append(int(a[i]))
        i+=1
l=len(b)
if k==0:
    for i in range(0,l):
        if i == len(b) - 1:
            print(b[i], end='')
        else:
            print(b[i], end=',')
else:
    for j in range(0,k):
        c = []
        for u in range(0, l-1):
            c.append(int(b[u + 1]) - int(b[u]))
        b=c
        l-=1
    for i in range(0,len(c)):
        if i==len(c)-1:
            print(c[i],end='')
        else:
            print(c[i],end=',')

#처음에는 이런식으로 콤마를 처리를 해 주었는데, 이런식으로 처리하면 10 이상의 수가 들어오면 '1','0'으로 나누어서 처리되어서 고민을 해 보았다.

n,k=map(int,input().split())
a=input().split(',')
if k==0:
    for i in range(0,n):
        if i==n-1:
            print(a[i])
        else:
            print(a[i],end=',')
else:
    for i in range(0,k):
        b=[]
        for j in range(0,n-1):
            b.append(int(a[j+1])-int(a[j]))
        n-=1
        a=b
    l = len(b)
    for i in range(0, l):
        if i == l - 1:
            print(b[i])
        else:
            print(b[i], end=',')

#한참을 고민하다 결국 split에 인자가 들어갈 수 있다는 것을 알게 되었고, k가 0일 때와 0이 아닐 때를 나누어서 처리를 해 주었다.
#문제는 수를 입력받으면 a[i+1]-a[i]로 새로운 수열을 만드는 것이였다.
#문제 자체는 간단하지만, 처리해 주어야 할 것이 꽤 많았다.
#심지어 값은 잘 나오지만 런타임 에러가 나온다.