# #문제
# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.


n=input()
while True:
    bool = True
    l = len(n)
    for i in range(0,l):
        if n[i].find('7') ==-1 and n[i].find('4')==-1:
            bool=False
            break

    if(bool):
        print(n)
        break
    n=str(int(n)-1)
