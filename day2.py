# a=2
# if(a<0):
#     print("a is negative")
# else:
#     print("a is positive")
# a=8
# if(a<0):
#      print("a is negative")
# elif(a==0):
#     print("number is zero")
# elif(a==8):
#     print("It is eight")
# else:
#      print("a is positive")
#      mathi ko first condition meet vayo vane tala ko herdai herdaina.
# n=8
# if(n<3):
#     print("positive")
# a="Ashmita"
# s=a.
#           1Grade :
# a=input("Enter your percentage")
# n=float(a)
# if n>=90 and n<=100 :
#     print("Distinction A+ grade")
# elif n>=80 and n<90:
#     print("Distinction A grade")
# elif n>=70 and n<80:
#     print ("First Division B+")
# elif n>=60 and n<70:
#     print ("Second Division B")
# elif n>=50 and n<60:
#     print ("Third Division C")
# else:
#     print("Fail")
#       2nestedif:
salary = float(input("Enter your salary"))
experience = float(input("Enter Your experience"))
performance = float(input("Enter your performance rating"))
 
department = input("Enter Your department")
 
if salary >= 25000:
    if experience >= 3:
        if performance >= 4:
            print("full Bonus")
        else:
            print("Partial Bonus")
    else:
        print("No Bonus")
 
elif salary<25000:
    if experience>=5 and performance ==5:
        print("Special Appreciation Bonus")
 
elif(department=="Sales" and Performance==5):
    print("Extra incentive")
else:
    print("Not eligible")
    print("Not eligible")    

