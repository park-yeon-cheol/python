# #문제
# A fish-finder is a device used by anglers to find fish in a lake. If the fish-finder finds a fish, it will sound an alarm. It uses depth readings to determine whether to sound an alarm. For our purposes, the fish-finder will decide that a fish is swimming past if:

# there are four consecutive depth readings which form a strictly increasing sequence (such as 3 4 7 9) (which we will call “Fish Rising”), or
# there are four consecutive depth readings which form a strictly decreasing sequence (such as 9 6 5 2) (which we will call “Fish Diving”), or
# there are four consecutive depth readings which are identical (which we will call “Constant Depth”).
# All other readings will be considered random noise or debris, which we will call “No Fish.”

# Your task is to read a sequence of depth readings and determine if the alarm will sound.

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a<b<c<d:
    print("Fish Rising")
elif a>b>c>d:
    print("Fish Diving")
elif a==b==c==d:
    print("Fish At Constant Depth")
else:
    print("No Fish")
