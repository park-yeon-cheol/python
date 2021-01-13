arr = [list(map(int, input().split()))for _ in range(9)]
result = max(map(max, arr))
print(result)
for i in range(0,9):
    for j in range(0,9):
        if arr[i][j]==result:
            print(i+1,j+1)

#이 문제는 2차원 배열에 입력을 받고, 최댓값을 찾은 후 그 인덱스+1을 하여 반환하면 되는 간단한 문제이다.
#하지만 2차원 배열이라 일반적으로 사용하는 max를 사용하지 못하고,
#max(map(max, arr))을 사용하였다.
#인덱스 출력을 이중 for문을 사용하지 않고, index함수를 사용하였지만,
#result의 값이 리스트에 없다고 나와서, numpy라는 외장 라이브러리 함수를 찾아보았다.
#myarr=np.array(arr,int), index=np.where(myarr==result) 로 사용해 보았는데,
#해당하는 인덱스 값은 나오지만, 다른 기호들이 같이 출력되어서 이중 for문을 사용하였다.