# #문제
# 2~15개의 서로 다른 자연수로 이루어진 리스트가 있을 때, 이들 중 리스트 안에 자신의 정확히 2배인 수가 있는 수의 개수를 구하여라.

# 예를 들어, 리스트가 "1 4 3 2 9 7 18 22"라면 2가 1의 2배, 4가 2의 2배, 18이 9의 2배이므로 답은 3이다.


while True:
    n = list(map(int, input().split()))
    if n[0]==-1:
        break
    result = 0
    l = len(n)
    for i in range(0, l - 1):
        result += n.count(n[i] * 2)
    print(result)

#while문으로 무한반복을 하고, -1이 입력되면 멈추도록 하였다.
#반복문을 통해서 n[i]*2가 n에 있을때 count함수를 사용해서 그 수를 더해주었다.