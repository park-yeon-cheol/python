# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

n = int(input())
result = 0
while True:
    if n % 5 == 0:
        result += n//5
        n = n - n//5*5
    else:
        n -= 3
        result += 1
    if n < 0:
        print(-1)
        break
    elif n == 0:
        print(result)
        break
       
#5로 나눠서 나누어 떨어지면 result에 5로 나는 몫을 더한 후 n을 초기화 해 주었다. 5로 나누어 떨어지지 않으면 3을 빼고 result에 1을 더해 주었다.
#n이 0이면 정확하게 나누어 떨어진 것이기 때문에 result를 출력하고 n이 음수가 나오면 정확하지 않기 때문에 -1을 출력해 주었다.
