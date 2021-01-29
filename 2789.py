a=list(map(str,input()))
for i in range(0,len(a)):
    if a[i]!='C' and a[i]!='A' and a[i]!='M' and a[i]!='B' and a[i]!='R' and a[i]!='I' and a[i]!='D' and a[i]!='G' and a[i]!='E':
        print(a[i],end='')


#주어진 단어에 'C,A,M,B,R,I,D,G,E'만 없으면 되므로 if문을 통해 해당하지 않을 때만 출력하도록 한다.