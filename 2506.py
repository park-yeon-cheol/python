import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
count=0
sum=0
for i in range(0,n):
    if a[i]==1:
        count=count+1
        sum=sum+count
    else:
        count=0
print(sum)

#이 문제는 정답을 연속해서 맞출 경우에 가산점을 부여하기 때문에
#입력받은 값이 1이면 count라는 변수의 값을 1씩 증가한 후,
#sum에 더해주면 되고, 만약 0이 나온다면 count의 값을
#다시 0으로 초기화해주면 된다.

