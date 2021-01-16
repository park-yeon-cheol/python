a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
result_x=result_y=0
if a[0]==b[0]:
    result_x=c[0]
elif a[0]==c[0]:
    result_x = b[0]
elif b[0]==c[0]:
    result_x = a[0]
if a[1]==b[1]:
    result_y=c[1]
elif a[1]==c[1]:
    result_y = b[1]
elif b[1]==c[1]:
    result_y = a[1]
print(result_x,result_y)

#x좌표는 각 x좌표끼리 비교하여 같은것이 있으면, 나머지 하나가 네 번째 점의 x좌표이다.
#y도 같은 방법으로 구해주면 된다.