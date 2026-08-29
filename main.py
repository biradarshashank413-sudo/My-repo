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
#for loop in python
# for letter in "python":
#     print(letter)
# for count in range(10,1,-1):
#     print(count)

# print("hello world!")
# ------------------------------------------------------------------------
#Star Pattern
# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
    
#     print()

# for i in range(1,4):

#     for j in range(3-i):
#         print(" ",end="")
#     for j in range(2 * i - 1): #Odd numbers are required for pyramid structure
#         print("*",end="")
#     print()

# # ------------------------------------------------------
# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")
# ----------------------------------------------------------/
#prime number
# n=int(input("enter the number: "))

# for i in range(2,n):
#     if(n%i)==0:
#         print("number is not prime")
#         break

# else:
#     print("number is prime")
# -----------------------------------------------------------------
#factorial number
# n=int(input("enter the number: "))
# product=1
# for i in range(1,n+1):
#     product=product*i
    
# print(f"the factorial number is {product}")
# ------------------------------------------------------------
#reverse multiplication
# n=int(input("enter the number: "))
# for i in range(10,0,-1):
#     print(f"{n} X {i} = {n*i}")
# ---------------------------------------------------------------------
# Fibonacci series
# a=0
# b=1
# for i in range(10):
#     print(a, end=",")

#     c=a+b
#     a = b
#     b = c
# ------------------------------------------------------------------
# palindrome series
# num=int(input("enter the number: "))
# temp = num
# reverse = 0
# while num>0:
#     digit = num % 10
#     reverse = reverse* 10 + digit
#     num = num //10

# if temp == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")
# ---------------------------------------------------------
#count number of digits 
# num = int(input("Enter the number: "))
# count = 0
# while num>0:
#     num = num // 10
#     count = count + 1

# print(f"The number count is {count}")
# --------------------------------------------------------
#sum of digits 
# num = int(input("enter the number: "))
# total=0
# while num>0:
#     digit=num%10
#     total=total+digit
#     num = num//10
# print("The sum of digits=",total)
# -----------------------------------------------------------------
#perfect number 
# num=int(input("enter the number: "))
# total=0
# i=1
# while i<num:
#     if num%i==0:
#         total=total+i
#     i=i+1

# if total==num:
#     print("Perfect number")
# else:
#     print("not perfect number")
# -----------------------------------------------------
#list 
# list=["apple","orange", 1,1.2,True]
# list[1]="mango"
# print(list[1:3])
# marks=[80,90,70]
# marks[1]=85
# print(marks)
# -----------------------------------------------------------
# l1=[[1,2,3],["alice", 32.3],["hale",True]]#nested list
# l1.sort()
# l1.reverse()
# l1.append(34)
# l1.insert(3,77)
# l1.extend([11,22,33])
# l1.count(3)
# l1.pop(2)#remove item by index value
# l1.remove(3)#remove item by direct value
# l1.clear()#give empty brackets
# print(l1[0])
# print(l1[1][0])
# print(l1[2][1])
# numbers=[1,2,3,4,5]
# print(9 in numbers)
# --------------------------------------------------------------------
#sum of all elements in a list
# number=[1,2,3,4,5]
# total=0
# for num in number:
#     total=total+num
# print(total)
# sum=sum(number)/len(number)#short method
# print(sum)
# --------------------------------------------------------
#largest number in list
# number=[1,2,3,4,5]
# largest=number[0]
# for num in number:
#     if num>largest:
#         largest=num

# print("Largest=",largest)
# print(max(number))
# print(min(number))
# count=0
# for num in number:#count of the list
#     count=count+1
# print("the count of numbers=",count)
# ---------------------------------------------------------------
# number=[1,2,3,3,4,4,4,4]
# print(number.index(3))#count the index number value
# print(number.count(3))# count how many times a number is repeated 
# ---------------------------------------------------
#print the number in reverse order
# number=[1,2,3,4,5]
# # number.reverse()# to print elements in reverse order 
# for num in number:
#     print(num)
# -----------------------------------------------------
#Tuple
# number=(1,2,3)
# # number[0]=23
# print(number)
# print(type(number))
# -------------------------------------------------------
# person=("alice",25,"trainner")
# a=(10,)
# print(type(a))
# print(type(person))
# name,age,role=person
# print(age)
# print(name)
# --------------------------------------------------
#tuple concatation
# a=(1,2,3)
# b=(4,5,6)
# c=a+b
# print(c)
#swapping of numbers easy
# a=10
# b=20
# print(a)
# print(b)
# a,b=b,a
# print(a)
# print(b)
# -------------------------------------------------------
# Write a program to accept marks of 3 students and display them in a sorted manner.
# marks=[]
# student1=int(input("enter the marks: "))
# marks.append(student1)
# student2=int(input("enter the marks: "))
# marks.append(student2)
# student3=int(input("enter the marks: "))
# marks.append(student3)
# marks.sort()
# print(marks)
number=(1,2,3,4,5,6)
# print(number[1:6:1])
# print(number[::-1])#reverse a tuple 