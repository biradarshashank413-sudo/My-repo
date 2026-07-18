# write a python program to convert text to speech using pyttsx3 library
# import pyttsx3

# engine = pyttsx3.init()

# engine.say("Hello Shashank, welcome to Python programming.")

# engine.runAndWait()
# ------------------------------------------------------------------------------

# a=print("enter the number")
# a=input()
# print(type(a))
# --------------------------------------------------------------------
# Write a python program to find an average of two numbers entered by the user.
# a=int(input("enter the number: "))
# print(f"the square of {a} is {a*a}")
# ---------------------------------------------------------------------
# text=" I like java"
# new_text=text.replace("java","python")
# print(new_text)
# ---------------------------------------------------------------
# name="hello world"
# print(len("helloworld"))
# ----------------------------------------------------------------------

# word="Shashank"
# print(word[::-1])
# -------------------------------------------------------------------

# word=input("Enter the text: ")
# print(word.upper())
# print(word.lower())
# print(word.capitalize())
# print(word.title())
# print(word.swapcase())
# -----------------------------------------------------------

# word="python java c++"
# print(word.split())
# print("".join(word))
# print("Python".isalpha())
# --------------------------------------------------------------
# Name=input("Enter the Name: ")
# print(f"Good Afternoon! {Name}")

# letter = """
# Dear <name>,

# You are selected!

# <Date>
# """
# print(letter.replace("<name>", "Alice"))
# print(letter.replace("<Date>", "27july26"))

# letter = "Dear Harry,\nthis python course is nice.\nThanks!"
# print(letter)
# -----------------------------------------------------------------
# age=int(input())
# if (age>=20):
#     print("eligible for vote")
# else:
#     print("not eligible for vote")

# marks=int(input("enter the marks: "))
# if marks>=90:
#     print("A+")
# elif marks>=80:
#     print("A")
# elif marks>=70:
#     print("B")
# else:
#     print("C")
# ----------------------------------------------------------------
# Write a program to find the greatest of four numbers entered by the user. 

# a=int(input("Enter the number1: "))
# b=int(input("Enter the number2: "))
# c=int(input("Enter the number3: "))
# d=int(input("Enter the number4: "))
# if a>b and a>c and a>d:
#     print(f"{a} is the greatest number")
# elif b>c and b>d and b>a:
#     print(f"{b} is the greatest number")
# elif c>d and c>a and c>b:
#     print(f"{c} is the greatest number")
# else:
#     print(f"{d} is the greatest number")

# -----------------------------------------------------------------

# Science=int(input("Enter the Science marks: "))
# maths=int(input("Enter the Maths marks: "))
# social=int(input("Enter the Social marks: "))

# Total = Science+maths+social
# percentage=(Total/300)*100

# if Science>=33 and maths>= 33 and social>=33:
#     if percentage>=40:
#         print("pass")
#     else:
#         print("fail")
# else:
#     print("fail")
# --------------------------------------------------------------------
# comment=input("Enter the chat: ").lower()
# if "Make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
#     print("spam detected")
# else:
#     print("not a spam")
# ----------------------------------------------
# name=input("enter user name: ")
# if len(name)>=10:
#     print("yes 10")
# else:
#     print("not 10")
# ---------------------------------------------------
# List=["harry","brook","alice"]
# name=input("enter ur name: ").lower()
# if (name in List):
#     print("your name in List")
# else:
#     print("your name is not there in List")
# -----------------------------------------------------
# match-case
# Day=int(input())
# match Day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case _:
#         print("Nothing!")
# -----------------------------------------------------
# LOOPS
# While loop
# count=10
# while count>=1:
#     print(count)
#     count -=1
# -----------------------------------------------------------
# multiplication table using while Loop
# num=int(input("enter the number:")) #Taking input
# count=0 #initialization

# print("the multiplication Number as follow as :")
# while count<=10: #condition
#     print(f"{num} X {count} = {num*count}") #statement
#     count+=1 #updation 

# ---------------------------------------------------------------------------
#break statement
# count=0
# while count<=10:
#     print(count)
#     if (count==5):
#         break #It will break loop and print upto 5 number instead of 10.
#     count +=1

# ---------------------------------------------------------------------------------
#continue statement , in order to skip the desired iteration(one round)
# count=0
# while count<=5:
#     if (count==3):
#         count +=1
#         continue
#     print(count)
#     count +=1
    # print("loop finished")
# ---------------------------------------------------------------------------
#break statement 
# count=0
# if count<=5:
#     pass
# print("finished")
# --------------------------------------------------------------------------
# Write a program to find the sum of first n natural numbers using while loop. 
# num=int(input("enter the number: "))
# count=1
# sum=0
# while count<=num:
#     sum=sum+count
#     count+=1

# print(sum)
# ----------------------------------------------------------------------------



