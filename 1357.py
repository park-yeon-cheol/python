# #문제
# 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.

# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

a,b=map(str,input().split())
a=a[::-1]
b=b[::-1]
result=str(int(a)+int(b))
print(int(result[::-1]))

#Rev에 맞게 입력받은 수를 역순으로 바꾼 후 int형으로 바꿔 더한 후 다시 역순으로 바꿔주었다.