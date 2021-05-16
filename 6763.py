# #문제
# Many communities now have “radar” signs that tell drivers what their speed is, in the hope that they will slow down.

# You will output a message for a “radar” sign. The message will display information to a driver based on his/her speed according to the following table:

# km/h over the limit	Fine
# 1 to 20	$100
# 21 to 30	$270
# 31 or above	$500

a=int(input())
b=int(input())
result=b-a
if result<=20 and result>=1:
    print("You are speeding and your fine is $100.")
elif result<=30 and result>=21:
    print("You are speeding and your fine is $270.")
elif result>=31:
    print("You are speeding and your fine is $500.")
elif result<=0:
    print("Congratulations, you are within the speed limit!")