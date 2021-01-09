n=list(map(int,input().split()))
if sum(n)>=100:
    print("OK")

else:
    if n[0]==min(n):
        print("Soongsil")
    elif n[1]==min(n):
        print("Korea")
    else:
        print("Hanyang")