#문제
#세 대각선이 한 점에서 만나지 않는 블록 n각형이 주어졌을 때, 대각선의 교차점의 개수를 세는 프로그램을 작성하시오. ->nC4

from itertools import combinations
n=int(input())
arr=[]
for i in range(0,n):
    arr.append(i)
a=list(combinations(arr,4))
print(len(a))

#조합 문제이기 때문에 처음에는 combination으로 풀었다.
#arr 리스트에 i로 채운 후, combinations(arr,4)를 사용하였다. 값은 잘 나오지만, 메모리 초과가 나타났다.

import math
n=int(input())
if n==3:
    print(0)
else:
    result = math.factorial(n) / (24 * math.factorial(n - 4))
    print(int(result))

#2번째에는 n이 3일때는 0을 출력하고, 4부터는 팩토리얼을 사용하여 풀어주었다.