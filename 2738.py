# 문제
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

n,m=map(int,input().split())    #2차원 배열 입력
arr=[[int(x) for x in input().split()]for y in range(n)]
arr1=[[int(x) for x in input().split()]for y in range(n)]
i=0
for i in range(n):
    result = []
    for j in range(m):
        result.append(arr[i][j]+arr1[i][j])
        print(result[j],end=' ')
    print()