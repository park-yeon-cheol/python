#문제
#N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

import sys
for _ in range(3):
    n=int(sys.stdin.readline())
    result = 0
    for _ in range(n):
        result=result+int(sys.stdin.readline())
    if result==0:
        print("0")
    elif result<0:
        print("-")
    else:
        print("+")

#처음에 입력을 int(input())으로 받으니 시간 초과가 나와서 sys.stdin.readline()으로 바꿔주니 해결되었다.