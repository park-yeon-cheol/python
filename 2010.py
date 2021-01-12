import sys
n=int(sys.stdin.readline())
a=[]
for i in range(0,n):
     a.append(int(sys.stdin.readline()))
# 처음에 sys.stdin.readline이 아닌 input으로 입력받았는데 시간 초과가
# 나왔다. 파이썬 입력받는 방법을 찾아보니 sys.stdin.readline으로 입력받는
# 방법이 있었다. input은 입력을 받고, 문자열로 변환 후, 개행을 벗겨내고 반환하기 때문에
# 오래걸린다 하지만 sys.stdin은 입력받는buffer을 따로 만들기 때문에 더 빠르다.
print(sum(a)-n+1)