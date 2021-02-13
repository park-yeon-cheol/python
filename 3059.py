# #문제
# 알파벳 대문자로 구성되어있는 문자열 S가 주어졌을 때, S에 등장하지 않는 알파벳 대문자의 아스키 코드 값의 합을 구하는 프로그램을 작성하시오.

# 문자열 S가 “ABCDEFGHIJKLMNOPQRSTUVW” 일 때, S에 등장하지 않는 알파벳 대문자는 X, Y, Z이다. X의 아스키 코드 값은 88, Y는 89, Z는 90이므로 이 아스키 코드 값의 합은 267이다.

t=int(input())
for _ in range(t):
    alpha=[0 for _ in range(26)]
    a=input()
    l=len(a)
    sum=0
    for i in range(0,l):
        idx=ord(a[i])-65
        alpha[idx]+=1
    for j in range(0,26):
        if alpha[j]==0:
            sum=sum+j+65
    print(sum)

#테스트 케이스를 t에 입력을 받고 반복문을 시작한다. alpha라는 리스트를 만들어서 A~Z를 나타내도록 한다. 문자열을 입력받고, 길이를 구한다.
#반복문을 통해 알파벳에 해당하는 인덱스를 구한 후 그 인덱스를 증가시켜 준다. 그 후 반복문을 통해 만약 alpha[j]의 값이 0이면 한번도 나오지 않은 것이기 때문에
#그때의 값의 아스키코드 값을 sum에 더해준다. 그 후 출력하면 된다.