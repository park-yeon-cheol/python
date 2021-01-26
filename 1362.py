count=1
while True:
    o,w=map(int,input().split())
    if o==0 and w==0:
        break
    else:
        dead = False
        while True:
            a, b = input().split()
            b = int(b)
            if w<=0:
                dead=True
            if a=='#' and b==0:
                break
            elif a=='F' and dead==False:
                w=w+b
            elif a=='E' and dead==False:
                w=w-b
        if w>o//2 and w<o*2:
            print(count,":-)")
        elif dead==True:
            print(count, "RIP")
        else:
            print(count,":-(")

        count+=1

#게임을 시작한 후, # 0을 입력 받으면 시나리오를 종료하고, 0 0을 입력 받으면 게임을 종료한다.
#E 숫자 를 입력 받으면 펫의 실제 체중이 숫자 만큼 감소하고
#F 숫자 를 입력 받으면 펫의 실제 체중이 숫자 만큼 증가한다.
#마지막에 실제 체중이 적정 체중의 1/2배를 초과하면서 적정 체중의 2배 미만이면 행복한 표정을 출력하고,
#죽었을 경우에는 RIP, 두 조건을 충족하지 못했을 때에는 슬픈 표정을 출력한다.
#처음에는 몇 번째 시나리오 인지 같이 출력하지 않아서 틀렸다.
#시나리오 번호까지 출력한 후, 계속 틀렸는데 그 이유가 dead로 설정해준 boolean type이 맨 첫번째에 있어서
#True인 상황에서 게임이 종료되면 False로 돌아가지 않고 True로 계속 유지되어서 틀렸었다.