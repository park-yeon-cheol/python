n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
if a[2]-a[1]==a[1]-a[0]:
    print(max(a)+(a[2]-a[1]))
else:
    print(max(a)*(a[2]//a[1]))

#수열이 주어지고, 규칙이 등차수열인지 등비수열인지 결정한 후 다음에 등장할 수를 구한다.
#처음에 수열의 길이n 을 입력 받고 리스트 a에 수를 입력받는다.
#n은 무조건 3이상이기 때문에 a[2]-a[1]==a[1]-a[0]을 통해 등차수열인지 비교를 해준다.
#만약 True이면 등차수열 이므로 max(a) 값에 공차를 더하면 되고,
#False라면 등비수열이므로 max(a)값에 공비를 곱하면 된다.