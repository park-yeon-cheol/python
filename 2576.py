odd=0
arr=[]
for i in range(0,7):
    n=int(input())
    if n%2!=0:
        odd=odd+1
        arr.append(n)
if odd==0:
    print(-1)
else:
    print(sum(arr),min(arr),sep='\n')

#7개의 자연수를 입력받고, 홀수인 자연수들을 모두 골라 합과최소인 홀수를 구하는 문제이다.
#홀수가 없으면 -1을 출력해야 하므로 odd라는 변수를 만들어서
#홀수가 없을 때를 확인해 준다.
#그 후, sum 함수와 min함수를 사용해 답을 출력한다.