# 문제
# 상근이는 길을 걷다가 신기한 기계를 발견했다. 기계는 매우 매우 큰 화면과 버튼 하나로 이루어져 있다.

# 기계를 발견했을 때, 화면에는 A만 표시되어져 있었다. 버튼을 누르니 글자가 B로 변했다. 한 번 더 누르니 BA로 바뀌고, 그 다음에는 BAB, 그리고 BABBA로 바뀌었다. 상근이는 화면의 모든 B는 BA로 바뀌고, A는 B로 바뀐다는 사실을 알게되었다.

# 버튼을 K번 눌렀을 때, 화면에 A와 B의 개수는 몇 개가 될까?

k = int(input())
a=['A']
def change(a,l):
    for _ in range(0,l):
        if a[0] == 'A':
            a.remove('A')
            a.append('B')
        else:
            a.remove('B')
            a.append('B')
            a.append('A')
    return a
l=1
for _ in range(0,k):
    change(a,l)
    l = len(a)
result_A=a.count('A')
result_B=len(a)-result_A
print(result_A,result_B)

#firt_try: 처음 입력이 A이기 때문에 배열에 넣어 두고 change 라는 함수를 만들었다. change 함수는 A이면 B로 바꾸고 B 이면 BA로 바꾸는 함수이다. 그 후 A와 B의 갯수를 count 하여 출력하였는데 시간 초과가 나왔다.

# 1 = 0 1
# 2 = 1 1
# 3 = 1 2
# 4 = 2 3

# 0 1 1 2 3 5 8 13 ...
#fib(0) = 0
#fib(1) = 1
#fib(2) = 1
#fib(3) = 2
# => fib(n-1), fib(n)

def fibo(n):
    result=0
    a=0
    b=1
    if n<2:
        return n
    else:
        for i in range(1,n):
            result=a+b
            a=b
            b=result
        return result
k=int(input())
print(fibo(k-1),fibo(k))

#규칙을 찾아보니 피보나치가 나왔다. k일때 fib(k-1), fib(k)가 나와서 피보나치 함수를 작성하여 구하였다.