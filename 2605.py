#문제
#학생들이 한 줄로 선 후, 첫 번째 학생부터 번호를 뽑는다. 첫 번째 학생은 무조건 0번을 뽑으며 제일 앞줄에 선다.
#다음 학생부터는 0~자신 차례-1 번의 번호를 뽑는다. 0번이면 제자리에 있고, 아니면 뽑은 번호만큼 앞자리로 가서 줄을 선다.
#학생들이 줄을 선 순서를 출력하라.
n=int(input())
num=list(map(int,input().split()))
arr=[]
index=1
for i in range(0,n):
    arr.insert(num[i],index)
    index+=1
arr.reverse()           #list=arr[::-1]
for i in range(0,n):
    print(arr[i],end=' ')

#n에 학생의 수를 입력 받고, num에 리스트로 학생들이 뽑은 번호를 입력받았다.
#뽑은 번호만큼 앞자리로 가는게 아니라 뒷자리로 간 후 뒤집어 주면 똑같은 결과가 나올 것이라 생각해서 arr리스트를 만들고
#그 리스트에 insert로 num[i]에 해당하는 index에 학생들 순서를 넣어 주었다. 그 후 reverse로 뒤집어주었다.
#reverse를 사용하지 않고 변수=arr[::-1]을 사용해 주어도 같은 결과가 나온다.