count=0

for i in range(0,8):
    arr=[]
    n=str(input())
    arr=n
    if i%2==0:
        for j in range(0,8):
            if j%2==0 and n[j]=='F':
                count+=1
    else:
        for j in range(0,8):
            if j%2==1 and n[j]=='F':
                count+=1
print(count)

#홀수와 짝수를 나누어서 생각을 해준다. (0,0)이 흰색이므로
#짝수줄은 짝수일 때 흰색이고, 홀수줄은 홀수일 때 흰색이다.
#그 후 'F'가 있는지 확인해 주면 된다.