a,b,c=map(int,input().split())
print(max(b-a,c-b)-1)

#캥거루 3마리를 a,b,c로 받고, 
#a에서 b, b에서 c까지의 거리를 구한 후,
#한 점에 캥거루 2마리가 있는 경우는 없으니
#max값을 구한 후 -1을 해주면 된다. 