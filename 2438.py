import sys
n=int(sys.stdin.readline())
for i in range(1,(n+1)):
    for j in range(1,i+1):
        print("*",end='')
    print()
#python에서의 print는 \n 처리가 자동으로 되어서 end=''을 통해 개행처리를 없애주었다.