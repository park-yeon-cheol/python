import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(0,n):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b==c:
        arr.append(10000+a*1000)
    elif a==b or a==c:
       arr.append(1000+a*100)
    elif b==c:
       arr.append(1000 + b * 100)
    else:
       arr.append(max(a,b,c)*100)
print(max(arr))
#세 개가 같을 때, 두 개가 같을 때, 다 다를 때로 케이스를 나누어 문제를 해결한다.