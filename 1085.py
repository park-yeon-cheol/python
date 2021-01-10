x,y,w,h=map(int,input().split())
arr=[x,y,w-x,h-y] #x,y좌표가 원점과 w,h중 더 가까운 곳을 출력하면 최소거리이다.
print(min(arr))
