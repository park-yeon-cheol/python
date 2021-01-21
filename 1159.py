n=int(input())
count=[0 for _ in range(26)]
for i in range(0,n):
    name=str(input())
    count[ord(name[0])-97]+=1
if max(count)<5:
    print("PREDAJA")
else:
    for j in range(0,26):
        if count[j]>=5:
            print(chr(j+97),end='')

#n을 통해 첫 줄에 선수의 수를 입력 받는다.
#count라는 배열을 만들어 0으로 초기화 시킨다.
#count배열은 알파벳에 따른 배열이다. 즉 a가 입력되면 count[0]이 1 증가한다.
#그 후 for문을 통해 선수의 이름을 입력받고, 
#ord를 통해 문자를 아스키 코드로 바꿔 준 후, 97을 빼서 index를 맞춰누다.
#다 입력받은 후 count의 값이 5보다 작은값들이면 "PREDAJA"를 출력하고,
#아니면 5 이상인 배열의 index를 가져와 chr(j+97)을 통해 원래의 알파벳으로 바꾸고 출력해준다.
