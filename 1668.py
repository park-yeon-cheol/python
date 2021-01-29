count=count2=1
n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
min=a[0]
for i in range(1,n):
    if a[i]>min:
        count+=1
        min=a[i]
print(count)
a.reverse()
max=a[0]
for i in range(1,n):
    if a[i]>max:
        max=a[i]
        count2+=1
print(count2)

#트로피의 개수 n을 입력받고, n개의 줄에 왼쪽의 트로피가 높이대로 주어진다.
#a 리스트에 입력을 받고, 왼쪽에서 볼때는 min=a[0]로 두고, 반복문을 돌려준다.
#만약 a[i]가 min보다 크다면 보이기 때문에 count를 증가시켜 주고 min을a[i]로 바꾸어 준다.(처음에 이 부분을 처리하지 않아 틀렸었다.)
#오른쪽에서 볼 때는 리스트a를 reverse 한 후 왼쪽에서 볼 때와 동일하게 해주면 된다.