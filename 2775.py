# #문제
# 평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

# 이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

def floor(k, n):
    if k == 0:
        global result
        result += zero_floor[n - 1]
    else:
        for i in range(1, n + 1):
            floor(k - 1, i)

t=int(input())  #테스트 케이스
zero_floor=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for _ in range(t):
    result = 0
    k = int(input())  # 층
    n = int(input())  # 호
    floor(k, n)
    print(result)

#재귀를 이용하여 작성해 보았지만 시간 초과가 나왔다.

t=int(input())  #테스트 케이스
for _ in range(t):
    result = 0
    k = int(input())  # 층
    n = int(input())  # 호
    floor = [n for n in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            floor[i] = floor[i] + floor[i - 1]
    print(floor[-1])

    #다음에는 단순하게 작성하였다. 반복문을 통하여 k층까지 반복하고, 위에 층의 사람 수를 구할때 옆방 + 아랫방을 더해주었다.