# #문제
# A CCC soccer game operates under slightly different soccer rules. A goal is only counted if the 4 players, in order, who touched the ball prior to the goal have jersey numbers that are in strictly increasing numeric order with the highest number being the goal scorer.

# Players have jerseys numbered from 1 to 99 (and each jersey number is worn by exactly one player).

# Given a jersey number of the goal scorer, indicate how many possible combinations of players can produce a valid goal.

from itertools import combinations
a=int(input())
arr=[]
i=1;
while i<a:
    arr.append(i)
    i=i+1
b=list(combinations(arr,3))

print(len(list(b)))