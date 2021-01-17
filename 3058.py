n=int(input())
for i in range(0,n):
    b = []
    a=list(map(int,input().split()))
    for j in range(0,7):
        if a[j]%2==0:
            b.append(a[j])
    print(sum(b),min(b))

#테스트 케이스를 n으로 입력받고, a에 리스트로 7개의 자연수를 입력받는다
#그 후 2로 나눈 나머지가 0이면 짝수이므로 b라는 리스트에 추가한다.
#b의 합과 b중 최소를 출력하면 된다.