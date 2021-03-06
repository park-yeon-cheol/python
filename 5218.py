# #문제
# 길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 알파벳 거리를 구하는 프로그램을 작성하시오.

# 두 글자 x와 y 사이의 알파벳 거리를 구하려면, 먼저 각 알파벳에 숫자를 할당해야 한다. 'A'=1, 'B' = 2, ..., 'Z' = 26. 그 다음 y ≥ x인 경우에는 y-x, y < x인 경우에는 (y+26) - x가 알파벳 거리가 된다.

# 예를 들어, 'B'와 'D' 사이의 거리는 4 - 2 = 2이고, 'D'와 'B' 사이의 거리는 (2+26) - 4 = 24이다.


n=int(input())
for _ in range(n):
    a, b = map(str, input().split())
    l = len(a)
    print("Distances:", end=' ')
    for i in range(0, l):
        x = ord(a[i])
        y = ord(b[i])
        if y >= x:
            print(y - x, end=' ')
        else:
            print(y + 26 - x, end=' ')
    print()

#테스트 케이스 n을 입력받고 반복문을 돌린다.
#a,b에 str로 입력받고, 글자의 길이 l을 구해준다.
#Distances: 을 출력해 주고 반복문을 통해 문자열을 비교해서 y>=x면 y-x, 그 외의 경우는 y+26-x를 해주었다.
#str로 입력받았기 때문에 비교를 위해 ord를 사용하여 아스키코드로 바꿔주었다.