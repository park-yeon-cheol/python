n=input()   #평문
s=input()   #암호화문
l1=len(n)
l2=len(s)
if l1==l2:
    for i in range(0,l1):
        if n[i]==' ':
            print(" ",end='')
        else:
            result1=ord(n[i])-96
            result2=ord(s[i])-96
            asc=result1-result2
            if asc<=0:
                print(chr(122+asc),end='')
            else:
                print(chr(96+asc),end='')
else:
    idx=0
    for i in range(0,l1):
        if idx==l2:
            idx=0
        if n[i]==' ':
            print(" ",end='')
            idx+=1
        else:
            result1=ord(n[i])-96
            result2=ord(s[idx])-96
            asc=result1-result2
            if asc<=0:
                print(chr(122+asc),end='')
            else:
                print(chr(96+asc),end='')
            idx+=1

#평문은 소문자와 띄어쓰기로 이루어져 있고, 암호화는 소문자로만 이루어져 있다. 띄어쓰기를 포함한 ㅍ쳥문과 암호화 키의 자리수가 같아야 하기 때문에, 암호와 키가
#평문과 길이가 같을 때와 적을 때로 나누어 주었다. 암호화 키에 해당하는 알파벳 순서를 가지고 평문의 문자를 그만큼 앞으로 당겨야 한다. a보다 적어지면 z로 돌아가야 하기 때문에
#if-else문으로 처리해 주었다.