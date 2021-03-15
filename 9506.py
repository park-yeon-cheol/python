# #문제
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다. 

# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.


while True:
    n=int(input())
    a=[]
    if n==-1:
        break
    for i in range(1,n):
        if n%i==0:
            a.append(i)
    l=len(a)
    if n==sum(a):
        print(n,end=' = ')
        for i in range(0,l):
            if i==l-1:
                print(a[i])
            else:
                print(a[i],end=' + ')

    else:
        print("{0} is NOT perfect.".format(n))

#while문으로 무한반복문을 설정해 놓고 n이 -1이면 종료되도록 해주었다.
#for문으로 n의 약수를 구하고 리스트 a에 넣어놓는다.
#리스트의 합과 n이 같으면 출력 형식에 맞춰 출력해 주었다.
