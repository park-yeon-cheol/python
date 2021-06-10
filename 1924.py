#문제
#오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

import calendar
day=["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x,y=map(int,input().split())
k=calendar.weekday(2007,x,y)

print(day[k])

#calendar.weekday를 사용하면 해당 년, 월, 일에 날짜를 알려준다.