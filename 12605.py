# 문제
# 스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때, 단어들을 반대 순서로 뒤집어라. 각 라인은 w개의 영단어로 이루어져 있으며, 총 L개의 알파벳을 가진다. 각 행은 알파벳과 스페이스로만 이루어져 있다. 단어 사이에는 하나의 스페이스만 들어간다.


n=int(input())
count=1
for _ in range(n):
    s=input().split()[::-1]
    l=len(s)
    print("Case #{0}: ".format(count),end='')
    for i in range(0,l):
        print(s[i],end=' ')
    count+=1
    #print()