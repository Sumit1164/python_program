# i = 0
# while i<10:
#     print('yes')
#     i = i+1

# f =1
# while f<=10:
#     k= f*2
#     print(k)
#     # print(f)
#     f=f+1

# f =1
# while f<50:
#     print(f)
#     f=f+1

# fruits = ['banana', 'apple', 'watermeloan', 'mangoes', 'grapes']
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i= i+1

# fruits = ['banana', 'apple', 'watermeloan', 'mangoes', 'grapes']
# for item in fruits:
#     print(item)

# for i in range(1,8):
#     print(i)

# for i in range(10):
#     print(i)
# else:
#     print("This is inside4 else of for")

# break statements
# for i in range(1,10):
#     print(i)
#     if i== 6:
#         break 

#continue statements
# for i in range(1,10):
#     if i==6:
#         continue 
#     print(i)

# pass statements
# i =4
# if i>0:
#     pass
# print("Sumit bhai!")


# pratic set ques1
# num = int(input("Enter a number"))
# for i in range(1,11):
#     print(str(num) +"X"+ str(i) +"="+ str(i*num))
#     print(f"{num}X{i}={num*i}") #f string method

# pratic set ques2
# l1=["SUMIT", "KALASH", "RAM", "RAHUL", "MAHIMA","KALU", "KASHISH"]
# for name in l1:
#     if name.startswith("S"):
#         print("HELLO "+name)
#     if name.startswith("KAS"):
#         print("GU KHA LE "+name+" BETA")
#     if name.startswith("M"):
#         print("I AM "+name+" I WANT TO SAY SOMTHING SUMIT I LOVE YOU")

# pratic set ques3
# num = int(input("Enter a number: "))
# prime= True
# for i  in range(2, num):
#     if (num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not Prime")

# pratic set ques6
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
#     print(factorial)
# print(factorial)
# print(f"The factorial of {num} is {factorial}")

# pratic set ques7
# n=10
# for i in range(10):
#     print(" " *(n-i-1), end="")
#     print("*" *(2*i+1), end="")
#     print(" " *(n-i-1))

# pratic set ques8
# n= 4
# for i in range(4):
#     print("*"*(i+1))

# pratic set ques10
num = int(input("Enter a number"))
for i in range(1,11):
    # print(str(num) +"X"+ str(i) +"="+ str(i*num))   
    print(f"{num}X{i}={num*i}")