arr=[]
for i in range(0,5):
    a=map(int,input().split())
    arr.append(sum(a))
print(arr.index(max(arr))+1,max(arr))

#간단한 문제이다.
#5명의 참가자의 네 개의 평가 점수를 입력받아
#sum 함수를 이용하여 합을 구한 후 arr배열에 넣고,
#index 함수와 max 함수를 사용하여 값을 구한다.