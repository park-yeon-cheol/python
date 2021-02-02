#문제
#세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
a=int(input())
b=int(input())
c=int(input())
arr=[0 for _ in range(10)]
result=str(a*b*c)
for i in range(0,len(result)):
    if result[i]=='0':
        arr[0]+=1
    elif result[i]=='1':
        arr[1]+=1
    elif result[i]=='2':
        arr[2]+=1
    elif result[i]=='3':
        arr[3]+=1
    elif result[i]=='4':
        arr[4]+=1
    elif result[i]=='5':
        arr[5]+=1
    elif result[i]=='6':
        arr[6]+=1
    elif result[i]=='7':
        arr[7]+=1
    elif result[i]=='8':
        arr[8]+=1
    elif result[i]=='9':
        arr[9]+=1

for i in range(0,10):
    print(arr[i])

#a,b,c를 정수로 입력 받아 곱한 후, result에 문자열로 넣어 주었다.
#반복문을 통해서  result의 길이만큼 반복하여, 0~9까지의 숫자가 나올 때 해당하는 배열을 증가시켜 주었다.

a=int(input())
b=int(input())
c=int(input())
result=str(a*b*c)
for i in range(10):
    print(result.count(str(i)))

#count함수는 문자열의 수를 계산해 준다.
#count를 사용하면 더 쉽게 해결이 가능하다.