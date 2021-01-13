import sys
for i in range(0,3):
    n = list(map(int, sys.stdin.readline().split()))
    if sum(n)==4:
        print("E")
    elif sum(n)==3:
        print("A")
    elif sum(n)==2:
        print("b")
    elif sum(n)==1:
        print("C")
    else:
        print("D")
#배가 나오는 경우가 0, 등이 나오는 경우가 1이므로
#n으로 입력받은 list의 합을 sum 함수를 이용하여 구하면
#등이 몇 번 나왔는지 알 수 있고, 이로 인해 도, 개, 걸, 윷, 모를 판별할 수 있다.




