# #문제
# 소수란 1과 자기 자신으로만 나누어떨어지는 수를 말한다. 예를 들면 1, 2, 3, 5, 17, 101, 10007 등이 소수이다. 이 문제에서는 편의상 1도 소수로 하자.

# 알파벳 대소문자로 이루어진 영어 단어가 하나 있을 때, a를 1로, b를 2로, …, z를 26으로, A를 27로, …, Z를 52로 하여 그 합을 구한다. 예를 들어 cyworld는 합을 구하면 100이 되고, abcd는 10이 된다.

# 이와 같이 구한 수가 소수인 경우, 그 단어를 소수 단어라고 한다. 단어가 주어졌을 때, 그 단어가 소수 단어인지 판별하는 프로그램을 작성하시오.

n=input()
l=len(n)
sum=0
for i in range(0,l):
    if n[i].islower():
        sum=sum+ord(n[i])-96
    else:
        sum=sum+ord(n[i])-38
count=0
for i in range(1,sum+1):
    if sum%i==0:
        count+=1
if sum==1:
    print("It is a prime word.")
elif count==2:
    print("It is a prime word.")
else:
    print("It is not a prime word.")


#n에 영어 단어를 입력 받고, 반복문을 통해서 각 단어를 ord를 이용해서 아스키 코드로 바꾸고 소문자이면 -96, 대문자이면 -38을 통해 1부터 52까지의 수로 만들었다.
#그 후 반복문을 통해서 소수 판별을 하고, 1일 경우를 소수로 처리했기 때문에 sum이 1일 때와 count가 2일때 소수이고, 그 외에는 소수가 아니다.