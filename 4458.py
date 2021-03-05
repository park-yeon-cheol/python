# #문제
# 문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.

n=int(input())
for _ in range(n):
    s = input()
    print(s.capitalize())

#처음에는 capitalize()함수를 사용해서 문자열의 첫 글자를 대문자로 바꿔주었다.
#하지만 powdered Toast Man 과 같은 문자열이 주어졌을때 T 와 M이 소문자로 바뀌었다.

n=int(input())
for _ in range(n):
    s = input()
    print(s[0].upper()+s[1:])

#upper() 함수를 사용하여 맨 첫 글자만 대문자로 바꿔주고 그 뒤에 문자열을 이어붙여 주었다.