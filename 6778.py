# #문제
# Canada Cosmos Control has received a report of another incident. They believe that an alien has illegally entered our space. A person who witnessed the appearance of the alien has come forward to describe the alien’s appearance. It is your role within the CCC to determine which alien has arrived. There are only 3 alien species that we are aware of, described below:

# TroyMartian, who has at least 3 antenna and at most 4 eyes;
# VladSaturnian, who has at most 6 antenna and at least 2 eyes;
# GraemeMercurian, who has at most 2 antenna and at most 3 eyes.

a=int(input())
b=int(input())
if a>=3 and b<=4:
    print("TroyMartian")
if a<=6 and b>=2:
    print("VladSaturnian")
if a<=2 and b<=3:
    print("GraemeMercurian")

