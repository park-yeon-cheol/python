while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        if c-b==b-a:
            print("AP", c+(c-b))
        elif c//b==b//a:
            print("GP", c*(c//b))

#c-b 와 b-a를 한 값이 같으면 등차수열이고
#c//b 와 b//a를 한 값이 같으면 등비수열이다.