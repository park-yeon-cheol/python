a=[]
for i in range(0,5):
    a.append(int(input()))
avg=sum(a)/5
a.sort()
print(int(avg),a[2],sep='\n')

#평균은 a를 모두 더한 후 5로 나누어 주었고, 중앙값은 a를 정렬한 후 a[2]의 값을 출력하였다.