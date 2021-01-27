alpha=[0 for _ in range(26)]
while True:
    try:
        s=input().replace(' ','')
        for i in range(0, len(s)):
            n = ord(s[i]) - 97
            alpha[n] = alpha[n] + 1
    except EOFError:
        break
result_max=max(alpha)
for j in range(0,26):
    if alpha[j]==result_max:
        print(chr(j+97),end='')

#EOF처리를 해주는 부분에서 어려움이 있었다.
#처음에는 if-else 문을 이용해서 s==''이면 break를 해주었는데, 이렇게 하면 엔터를 두 번 쳐야해서
#try except EOFError를 사용해 주었다.
#입력을 한 후ctrl-D를 사용해서 eof처리를 해준다.