# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

n=int(input())
for i in range(0,n):
    a, b = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1,a,b,a+b))