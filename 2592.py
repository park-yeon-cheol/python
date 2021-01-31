import numpy
from collections import Counter
a=[]
for _ in range(10):
    a.append(int(input()))
c=Counter(a)
mode=c.most_common(1)
print(int(numpy.mean(a)))
print(mode[0][0])

#numpy와 Counter을 사용하여 평균과 최빈값을 구하는 법을 알았다.
#하지만 백준에서는 런타임 에러 (ModuleNotFoundError)라고 하여 다시풀었다.

a=[]
most=[0 for _ in range(1000)]
for i in range(0,10):
    a.append(int(input()))
    most[a[i]-1]+=1
avg=sum(a)/10
r_most=most.index(max(most))+1
print(int(avg),r_most,sep='\n')

#입력받는 수가 1000 이하이기 때문에 0으로 채운 1000개의 리스트를 만들어 주고, 입력받을 때마다 해당하는 인덱스에 +1을 해주었다.
#평균은 리스트를 모두 더한 후 10으로 나누어 주었고, 최빈값은 가장 큰 most리스트의 값의 인덱스를 가져왔다.
