# 문제
# 앞 면에 O와 X가 적혀있는 카드 N개가 있다. N개의 카드 중 M개의 카드의 앞면에는 O가 한 개 적혀있고, 나머지 N-M개의 카드의 앞면에는 X가 한 개 적혀있다. 카드의 뒷 면은 두 종류의 카드 모두 같은 모양이라 구분할 수 없다.

# 카드의 뒷 면에 O나 X를 하나씩 적으려고 한다. 이 때, O는 K개, X는 N-K개 적으려고 한다.

# 앞 면과 뒷 면에 같은 모양이 적혀있는 카드의 최대 개수를 구하는 프로그램을 작성하시오.

n,m,k=map(int,input().split())
result=0
if m-k>=0:
    result=result+k+(n-m)
    print(result)
else:
    result=result+m+(n-k)
    print(result)


