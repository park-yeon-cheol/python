# #문제
# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

# 1234567891011121314151617181920212223...

# 이렇게 만들어진 새로운 수에서 N이 등장하는 위치를 알고 싶다. 물론 1부터 N까지의 수를 이어 쓰는 것이므로 수의 가장 끝부분에서 N이 항상 등장하게 되지만, 그보다 일찍 등장하는 경우도 있다.

# 예를 들어 N=151인 경우, 다음과 같이 앞에서 20번째 숫자부터 151이 등장하게 된다.

# 1234567891011121314151617181920212223...

# N이 주어졌을 때, N이 가장 먼저 등장하는 위치를 알아내는 프로그램을 작성하시오.

n=input()
a=[]
for i in range(1,100001):
    a.append(str(i))
ans="".join(a)
result=ans.find(n)
print(result+1)

#리스트 a에 1~ 100000 까지의 수를 입력받고, join함수를 이용하여 공백없이 붙여서 만들어 주었다. 그 후 find함수를 사용하여 입력받은 n의 위치를 찾아주었다.