a=list(map(int,input().split()))

b=sorted(a)
x=b[2]-b[1]
y=b[1]-b[0]

if x==y:
    print(b[2]+x)
elif x>y:
    print(b[2]-y)
else:
    print(b[1]-x)

#등차수열을 구하는 문제이다.
#x와 y의 값이 같으면 그 다음에 나올 수 or 그 전에 나올 수이고,
#같지 않으면 중간에 나와야 할 수를 찾는다.