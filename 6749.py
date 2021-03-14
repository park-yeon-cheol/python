# #문제
# You know a family with three children. Their ages form an arithmetic sequence: the difference in ages between the middle child and youngest child is the same as the difference in ages between the oldest child and the middle child. For example, their ages could be 5, 10 and 15, since both adjacent pairs have a difference of 5 years.

# Given the ages of the youngest and middle children, what is the age of the oldest child?

a,b=map(int,input().split())
print(b*2-a)

#가장 나이가 많은 사람의 나이를 구하는 문제이다.