#문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.


alpha=[0 for _ in range(26)]
s=input()
l=len(s)
for i in range(0,l):
    if s[i].isupper():
        n=ord(s[i])-65
        alpha[n]+=1
    else:
        n = ord(s[i]) - 97
        alpha[n] += 1
m=max(alpha)
num=alpha.count(m)
if num>1:
    print("?")
else:
    result=alpha.index(m)
    print(chr(result+65))

#일단 알파벳이 몇번 사용되었는지 알아야 하기 때문에 alpha 라는 리스트를 만들어 알파벳 수 만큼 0으로 채워주었다.
#그 후 문자열을 입력받고, 길이를 구해 반복문을 작성하였다.
#s[i]의 값이 대문자이면 ord()를 통해 아스키코드로 바꾼 후 65를 빼주었고, 소문자라면 97을 빼주고 해당하는 인덱스에 alpha값을 증가시켜 주었다.
#max()함수로 가장 큰 값을 구하고, count()함수를 통해 중복된 값이 있는가를 체크해 주었다.
#만약 num이 1보다 크면 중복된 값이 있다는 뜻이기 때문에 "?"를 출력하였고, 크지 않을 때에는 해당하는 인덱스를 가져와 chr을 통해 다시 알파벳으로 돌려주었다.
#65를 더해 대문자로 만들었다.