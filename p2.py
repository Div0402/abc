"""x = 'Hello world'
x.split()
print(x)"""

"""name = input("name : ")
age = int(input("my age is : "))
salary = float(input("Total salary : "))
print("Your name is : ", name , "\nYour age is : ", age ,  "\nYour salary : " , salary)"""

#User input Arithmetic operator 

"""a = int(input("Enter number = "))
b = int(input("Enter number = "))

print("Press 1 for Addition : ")
print("Press 2 for Subtraction : ")
print("Press 3 for Multiplication : ")
print("Press 4 for Division : ")

Choice = int(input("Enter Your Choice : "))


if(Choice == 1):
    print("Your answer is " , a+b)
elif(Choice == 2):
    print("Your answer is ", a-b)
elif(Choice == 3):
    print("Your answer is ", a*b)
elif(Choice == 4):
    print("Your answer is ", a/b)
else:
    print("You Enter invalide number please press a between number 1 to 4")"""


"""Mark = int(input("Enter your Mark = "))

if(Mark >=90):
    print("A+ Grade")
elif(Mark >= 80 and Mark < 90):
    print("A Grade")
elif(Mark >= 70 and Mark < 80):
    print("B+ Grade")
elif(Mark >= 60 and Mark < 70):
    print("B Grade")
elif(Mark >= 50 and Mark < 60):
    print("C+ Grade")
elif(Mark >= 40 and Mark < 50):
    print("C Grade")
else:
    print("You are Fail")"""


# Many value for multiple variable


"""a,b,c = "Red", "Blue", "White"
print(a)
print(b)
print(c)
"""

# Unpacke a collection

"""color = ["Red", "Green", "Blue"]
r,g,b = color
print(r)
print(g)
print(b)"""


# Global Vriable     - Vriable are created outside of function is called global variable  ((  Globale variable is used by every one both inside and out side ))

"""a = "Div"           #this is global variable
def myfunc():
    print("My name is", a)
myfunc()"""

            # To create a global variable inside a function, you can use the global keyword.
            
"""a= "Div"
def myfunction():
   global b 
   b= "Lathiya"
myfunction()
print("Hello, My name is", a, b)"""

            #   Type conversion

"""a = "4"
b = 5.25
sum = int(a) + int(b)
print(sum)"""

        # Question :- Write a program to input 2 umber and print their sum

"""a = int(input("Enter Number :- "))
b = int(input("Enter Number :- "))
print("Your answer is ",a+b)"""

        # Question :- Write a program to input side of a square and print its area.

"""side = float(input("Enter square size : "))
area = side * side
print("Square area is ", area)
"""
        # Question :- Write a program to input floating point numbers and prrint their average 

"""a = float(input("Enter First value : "))
b = float(input("Enter First value : "))
print("Average = ", (a+b)/2)"""

        # Question :- Write a program to input 2 int numbers a and b. print True if a is geater than or equal to b. if not print false 

"""a = int(input("Enter First value : "))
b = int(input("Enter First value : "))
if(a>=b):
    print("True")
else:
    print("False")"""



                                        # String

# Topic Slicing    --- Accessign part of a string

"""name = "Div Lathiya"
print(name[0:4])
print(name[:6])
print(name[0:])
print(name[4:])"""

    # Negetive Index Slicing


name = "LATHIYA"
print(name[-1:-7])