while True:
    n=list(map(int,input()))    #호수판에 들어갈 숫자를 입력받는다.
    if n[0]==0: #0이 들어오면 종료해야 하므로 break 설정
        break
    else:
        result=0
        for i in range(0, len(n)):  #for문을 사용해서 각 숫자 당 필요한 길이를 받는다.
            if n[i]==1:
                result=result+2
            elif n[i]==0:
                result=result+4
            else:
                result = result + 3
    print(result+len(n)+1)  #각 숫자 사이의 간격 + 호수판 여백이니 숫자의 길이 +1을 해주면 된다.
