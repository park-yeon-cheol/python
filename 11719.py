# 문제
# 입력 받은 대로 출력하는 프로그램을 작성하시오.

n=[]
while True:
    try:
        n.append(input())
    except EOFError:
        break
l=len(n)
for i in range(0,l):
    print(n[i])