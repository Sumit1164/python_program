# if-elif-else ladder in python
# a = int(input("enter number"))
# if(a>3):
#     print("the value of a is greater than 3")
# elif(a>7):
#     print("the value of a is greater than 7")
# else:
#     print("the value is not greater tahn 3 or 7")
# print("done")
# quick quig
# age = int(input("Enter your age\n:"))
# if age>18:
#     print("yes")
# else:
        # print("no")



# relational operator
#  == 
#  >=


# logical operator   
# age = int(input("Enter your age: "))
# if(age>34 and age<56):
#         print("You can work with us")
# else:
#         print("You can not work with us")


# am = int(input("Enter your age: "))
# if(am>34 or am<56):
#         print("You can work with us")
# else:
#         print("You can not work with us")


# is and in uses
# a = None
# if (a is None):
#     print("yes")
# else:
#     print("noo")
# b = [45, 567, 980]
# print(45 in b)


# else is optional,you want then use else 
# a =76
# if(a==7):
#     print("Yes")
# elif(a>56):
#     print("no and yes")
# else:
#     print("i am conditional")



#  pratics set chap6 ques1

# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))
# num4 = int(input("Enter number 4 : "))
# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4
# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3
# if(f1>f2):
#         print(str(f2) + "is greatest")
# else:
#         print(str(f1) + "is greatest")
        
# pratics set chap6 ques2

# sub1 = int(input("Enter subject 1  marks\n: "))
# sub2 = int(input("Enter subject 2 marks\n: "))
# sub3 = int(input("Enter subject 3 marks\n: "))
# if(sub1<33 or sub2<33 or sub3<33):
#     print("YOU ARE FAIL")
# elif(sub1+sub2+sub3)/3 <40:
#     print("YOU ARE FAIL DUE TO TOTAL PERCENT LESS THAN 40")
# else:
#   print("YOU ARE PASSED THE EXAM")

# pratics set chap6 ques3
# text = input("Enter the text\n")
# spam =  False

# if("make a lot of money" in text):
#     spam = True
# elif("Buy now" in text):
#     spam = True
# elif("Click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam =  False
# if(spam):
#         print("This text is spam")
# else:
#         print("This text is not spam")

# pratics set chap6 ques4
username = input("Enter your name\n")
lessthan = True
if("less than 10" in username):
     lessthan = True
if(lessthan):
    print("the character is less than 10")
else:False
print("this text is not less than 10")
