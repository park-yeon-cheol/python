#문제
#해밍 거리란 두 숫자의 서로 다른 자리수의 개수이다. 두 이진수가 주어졌을 때, 해밍 거리를 계산하는 프로그램을 작성하시오.

t=int(input())
for _ in range(t):
    a=input()
    b=input()
    l=len(a)
    count=0
    for i in range(0,l):
        if a[i]!=b[i]:
            count+=1
    print("Hamming distance is %d."%count)

#테스트 케이스 t를 입력 받고 t 만큼 반복해 주었다. 이진수 두 개를 입력받고, 반복문을 통해서 같은지 다른지 비교해 주었다.
#다를때 count를 증가시켜 해밍거리를 구했다.