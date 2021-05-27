# #문제
# 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.

# 삼각형의 세 각을 입력받은 다음, 

# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.

a=[]
for i in range(3):
    a.append(int(input()))
sum=sum(a)
if a[0]==a[1]==a[2]==60:
    print("Equilateral")
elif sum==180 and (a[0]==a[1] or a[1]==a[2] or a[0]==a[2]):
    print("Isosceles")
elif sum==180:
    print("Scalene")
else:
    print("Error")