import sys
arr=[]
n,k=map(int,sys.stdin.readline().split())
for i in range(1,n+1):
    if n%i==0:
        arr.append(i)
if len(arr) < k:
    print(0)
else:
    print(arr[k-1])

#약수를 구하는 문제이다.
#for 문을 사용하여 1~n까지의 수 중 나머지가 0이 되는 수를 찾아
#arr이라는 배열에 저장한다.
#만약 배열의 길이보다 k 값이 크다면 0을 출력하고,
#그렇지 않으면 k-1 번째 값을 출력한다.


