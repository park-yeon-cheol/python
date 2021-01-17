num=1
while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        if c==max(a,b,c):
            if c>=a+b:
                print("Invalid")
            else:
                if a==b==c:
                    print("Equilateral")
                elif a==b or b==c or a==c:
                    print("Isosceles")
                else:
                    print("Scalene")
        elif b==max(a,b,c):
            if b>=a+c:
                print("Invalid")
            else:
                if a==b==c:
                    print("Equilateral")
                elif a==b or b==c or a==c:
                    print("Isosceles")
                else:
                    print("Scalene")
        elif a == max(a, b, c):
            if a >= c + b:
                print("Invalid")
            else:
                if a == b == c:
                    print("Equilateral")
                elif a == b or b == c or a == c:
                    print("Isosceles")
                else:
                    print("Scalene")

#Invalid의 경우를 고려하느라 코드가 매우 길어졌다.
#변의 길이를 비교해서 맞는 정의를 출력하면 된다.