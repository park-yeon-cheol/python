a,b=list(map(str,input().split()))
sum=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        sum+=int(a[i])*int(b[j])
print(sum)

#처음에 이중 for문으로 작성하였는데 시간 초과가 나왔다.
#그래서 다른 방법을 생각해 보았다.

a,b=list(map(str,input().split()))
result=0
sum_b=0
for j in range(0,len(b)):
       sum_b+=int(b[j])
for i in range(0,len(a)):
       result+=int(a[i])*sum_b
print(result)

#이중 for문 이기 때문에 시간복잡도가 n^2이 되어서 시간 초과가 나왔다.
#그래서 b의 합을 구하는 for문을 하나 만들고,
#b의 합과 리스트로 만들어 놓은 a를 곱하는 for문을 만들었다.

