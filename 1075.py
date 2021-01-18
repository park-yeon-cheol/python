n=int(input())
f=int(input())
a=n//100
for i in range(0,100):
    if i<10:
        result=a*100+i
        if result%f==0:
            print('{0}{1}'.format(0,i))
            break
    else:
        result = a * 100 + i
        if result%f==0:
            print(i)
            break

#정수 n의 가장 뒤 두 자리를 바꿔서 n을 f로 나눴을 때
#나누어 떨어지게 만들기 때문에 마지막 두 자리를 제외한 나머지를 a라고 한다
#만약 맨 뒤 수가 한자리이면 앞에 0을 붙여 2자리로 만들어야 하기 때문에 if문을 통해 구분을 해 준다.
#0~99까지 있으니 range를 0~100으로 설정해 준다.
#그 후 i를 통해 모든 숫자의 경우를 따진 수 출력해 준다.