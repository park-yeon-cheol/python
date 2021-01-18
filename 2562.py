n=[]
for i in range(0,9):
    n.append(int(input()))
print(max(n),n.index((max(n)))+1,sep='\n')

#자연수 9개를 리스트 n에 입력 받고, max값과 그에 해당하는 index+1을 해주면 된다.