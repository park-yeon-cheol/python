#문제
#5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.
#FBI요원은 요원의 첩보원명에 FBI가 들어있다. 

count=[]
for i in range(0,5):
    n = input()
    if len(n)>2:
        for j in range(0,len(n)-2):
            if n[j]=='F'and n[j+1]=='B' and n[j+2]=='I':
                count.append(i+1)
                break
if not count:
    print("HE GOT AWAY!")
else:
    for i in range(0,len(count)):
        print(count[i],end=' ')

#문자열을 입력받아 연석되는 세 개의 문자가 FBI이면 리스트 count에 그때의 인덱스+1을 추가해 주었다.
#count가 비어있으면 HE GOT AWAY!를 출력하도록 하였고, 그렇지 않으면 공백으로 값을 출력하였다.

count=[]
for i in range(5):
    n=input()
    if n.find("FBI") != -1:
        count.append(str(i+1))
if not count:
    print("HE GOT AWAY!")
else:
    print(" ".join(count))  

#위와 같은 방법으로 find를 사용하여 더 간단하게 풀 수 있다.