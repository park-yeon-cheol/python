# 문제
# Each player in a tournament plays six games. There are no ties. The tournament director places the players in groups based on the results of games as follows:

# if a player wins 5 or 6 games, they are placed in Group 1;
# if a player wins 3 or 4 games, they are placed in Group 2;
# if a player wins 1 or 2 games, they are placed in Group 3;
# if a player does not win any games, they are eliminated from the tournament.
# Write a program to determine which group a player is placed in

w=0
l=0
for i in range(0,6):
    a=input()
    if a == 'W':
        w=w+1
    else:
        l=l+1

if w==5 or w==6:
    print(1)
elif w==3 or w==4:
    print(2)
elif w==1 or w==2:
    print(3)
else:
    print(-1)
