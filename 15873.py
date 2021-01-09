a=int(input())
if a//1000!=0:
    print(20)
elif a//100!=0 and a%10==0:
    print((a//100)+10)
elif a//10!=0:
    print(a//10+a%10)
elif a//1000:
    print(a // 10 + a % 10)