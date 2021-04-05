# #문제
# 이 문제에서 당신은 Quicksum이라고 하는 checksum 알고리즘을 구현해야 한다.  Quicksum 패킷은 오직 대문자와 공백으로 이루어져있다. 그리고 시작과 끝은 항상 대문자이다.  공백은 문자와 섞여있을수 있으며 연속되어서 있을수도 있다.

# Quicksum은 각각의 문자의 위치와 문자 값의 합이다. 공백은 0이다. 문자는 고유의 위치값을 가지고 있는데 예를들어 A=1, B=2 ... Z=26이다.

# 예제 문장은 "ACM" 과 "MID CENTRAL"인데 살펴보면 다음과 같다.

# ACM: 1*1  + 2*3 + 3*13 = 46

# MID CENTRAL: 1*13 + 2*9 + 3*4 + 4*0 + 5*3 + 6*5 + 7*14 + 8*20 + 9*18 + 10*1 + 11*12 = 650


while True:
    s = input()
    if s[0]=='#':
        break;
    l = len(s)
    sum = 0
    for i in range(0, l):
        if s[i] == ' ':
            continue;
        n = ord(s[i]) - 64
        sum = sum + (i + 1) * n
    print(sum)

#무한반복을 통해 s[0]='#'일 때 종료하게 해 주었다.
#문자의 길이만큼 반복문을 통해 만약 공백이면 계속 진행하고, 그렇지 않은 경우에는 ord를 사용하여 아스키코드로 바꾼 수, i+1을 한 값과 곱해서 더해주었다.