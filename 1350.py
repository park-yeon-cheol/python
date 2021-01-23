n=int(input())
file=list(map(int,input().split()))
cluster=int(input())
size=0
for i in range(0,n):
       if file[i]!=0:
              if file[i]%cluster==0:
                     size=size+file[i]//cluster
              else:
                     size = size + file[i] // cluster+1
print(size*cluster)

#간단한 문제이지만, 파일 사이즈와 클러스터의 크기가 주어졌을 때의 수를 처리하지 못해서 틀렸었다.
#크기가 0인 파일은 클러스터가 필요 없고,
#파일과 클러스터 크기가 주어지면 그 몫이 파일의 수이고,
#그 나머지는 파일과 클러스터를 나눈 몫에 +1을 해준 후
#모두 더하고, 클러스터를 곱해서 출력하면 된다.