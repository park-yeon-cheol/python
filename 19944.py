n,m=map(int,input().split())
if m==1 or m==2:    #1학년, 2학년일때
    print("NEWBIE!")
elif m<=n:  #1,2학년이 아니지만 n학년 이하일때  
    print("OLDBIE!")
else:   #뉴비도 아니고 올드비도 아닐 때
    print("TLE!")

