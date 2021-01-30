a,b=input().split()
a=int(a)
b=int(b)
q,w,e,r,t=input().split()
q=int(q)
w=int(w)
e=int(e)
r=int(r)
t=int(t)
print(q-a*b,w-a*b,e-a*b,r-a*b,t-a*b)

#a*b를 한 후 입력받은 다섯 개의 숫자에서 빼주면 된다.
#a*b를 계속해서 사용하지 않고 변수로 미리 선언해 놓으면
#메모리를 줄일 수 있다.