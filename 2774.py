t=int(input())
for _ in range(t):
    num=[0 for _ in range(10)]
    count=0
    a=list(map(int,input()))
    for i in range(0,len(a)):
        num[a[i]]+=1
    for j in range(0,10):
        if num[j]>=1:
            count+=1
    print(count)

#테스트 케이스 t를 입력받고, 그 다음 아름다운 정도를 알고 싶은 수 x를 입력받는다.
#10진수의 중복되지 않은 숫자의 개수를 출력하면 되기 때문에,
#num이란 0~9까지를 나타내는 리스트를 만들고 입력받은 수를 자릿수마다 잘라 해당하는 인덱스의 값을 증가시켜준다.
#만약 num의 값이 1 이상이면 한번 이상 사용되었으므로 count해주면 된다.