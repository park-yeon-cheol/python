while True:
       a=list(map(str,input()))
       count=0
       if a[0]=="#":
              break
       else:
              for i in range(0,len(a)):
                     if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U':
                            count+=1
       print(count)


#영어 문장을 입력받아 모음의 개수를 세는 프로그램이다.
#모음은 'a,e,i,o,u' 이고, 대문자 이거나 소문자 이기 때문에
#if 문에 조건을 만들어주어서 해당하면 count를 +1 해준다.