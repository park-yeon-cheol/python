import calendar
m,d=map(int,input().split())
result=calendar.weekday(2009,m,d)
if result==0:
    print("Monday")
elif result==1:
    print("Tuesday")
elif result==2:
    print("Wednesday")
elif result==3:
    print("Thursday")
elif result==4:
    print("Friday")
elif result==5:
    print("Saturday")
elif result==6:
    print("Sunday")

#간단하게 calendar 라이브러리를 사용하였다.
#백준에 제출하니 ValueError가 나온다.
#이유는 잘 모르겠다.