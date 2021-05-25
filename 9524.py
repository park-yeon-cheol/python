# #문제
# Yekaterinburg is a beautiful city founded in the eighteenth century. Your task in this problem is to give us information about the precise year of its foundation.

# To make the task less overwhelming, you are only asked to calculate one of the four digits of the year. To indicate the position of the digit you must calculate, digits are numbered between 1 and 4, from the most significant to the least significant. As an example, for the year 2013 digit 1 is “2”, digit 2 is “0”, digit 3 is “1” and digit 4 is “3”.

# In case you failed to bring an encyclopedia with you, information about Yekaterinburg may be obtained via a clarification.

a=int(input())
if a==1:
    print(1)
elif a==2:
    print(7)
elif a==3:
    print(2)
elif a==4:
    print(3)