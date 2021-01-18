def registance(s,n):
    if s=='black':
        if n<2:
            return 0
        else:
            return 1
    elif s=='brown':
        if n < 2:
            return 1
        else:
            return 10
    elif s=='red':
        if n<2:
            return 2
        else:
            return 100
    elif s=='orange':
        if n<2:
            return 3
        else:
            return 1000
    elif s=='yellow':
        if n<2:
            return 4
        else:
            return 10000
    elif s=='green':
        if n<2:
            return 5
        else:
            return 100000
    elif s=='blue':
        if n<2:
            return 6
        else:
            return 1000000
    elif s=='violet':
        if n<2:
            return 7
        else:
            return 10000000
    elif s=='grey':
        if n<2:
            return 8
        else:
            return 100000000
    elif s=='white':
        if n<2:
            return 9
        else:
            return 1000000000
a=input()
b=input()
c=input()
print((registance(a,0)*10+registance(b,1))*registance(c,2))

#저항에 대한 값을 케이스 별로 나눠서 registance라는 함수로 만들어 주었다.
#그 후 계산을 해준다.
#dictionary로 구현하려 했으나, 곱의 값을 처리하려면 또 따로 만들어 주어야 해서
#함수로 만들어 한번에 처리해 주었다.