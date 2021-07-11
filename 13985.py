# 문제
# You are grading an arithmetic quiz. The quiz asks a student for the sum of the numbers. Determine if the student taking the quiz got the question correct.


a=list(map(str,input().split()))
if int(a[0])+int(a[2])==int(a[4]):
    print("YES")
else:
    print("NO")
