#문제
#수 124를 뒤집으면 421이 되고 이 두 수를 합하면 545가 된다. 124와 같이 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되는지 테스트 하는 프로그램을 작성하시오.
t=int(input())
for _ in range(t):
    n=input()
    a=n[::-1]
    result=str(int(n)+int(a))
    if result==result[::-1]:
        print("YES")
    else:
        print("NO")

#문자열로 입력받아서 [::-1]을 통해 뒤집어 주었다.
#그 후 원래 값과 뒤집은 값을 더해서  result에 저장하고, result와 result를 뒤집은 값이 같으면 좌우 대칭이기 때문에
#if문을 통해 비교해 주었다.