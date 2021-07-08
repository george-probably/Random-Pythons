"""
Created by George Chachanidze
Date: 30/10/2012
Purpose: Calculator
"""
import time
def menu():
    print ("Welcome to super awesome calculator v0.1")
    print ("")
    print ("1) Add 2 numbers")
    print ("2) Subtract 2 numbers")
    print ("3) Multiply 2 numbers")
    print ("4) Divide 2 numbers")
    print ("5) Square a number")
    print ("6) Squareroot a number")
    print ("7) Cube a number")
    print ("8) Cuberoot a number")
    print ("10) Exit")
    return int(input("Select your choice"))
"""
def menu2():
    print ("Welcome to more calculations!")
    print ("It's a secret menu!!")
    print ("")
    print ("WIP")
    print ("")
"""
def add (number, number2):
    print (number, "+", number2, "=", number+number2)

def sub (number, number2):
    print (number, "-", number2, "=", number-number2)

def multiply (number, number2):
    print (number, "*", number2, "=", number*number2)

def div (number, number2):
    print (number, "/", number2, "=", number/number2)

def square (number):
    print (number, "Squared =", number**2)

def squareroot (number):
    print ("The Squareroot of", number, "=", number**0.5)

def cube (number):
    print (number, "Cubed =", number**3)

def cuberoot (number):
    print ("The Cuberoot of", number,"=", int (number**(1/3)))

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(int(input("Enter your first number")),int(input("Enter your second number")))
    elif choice == 2:
        sub(int(input ("Enter your first number")),(int(input("Enter your second number"))))
    elif choice == 3:
        multiply(int(input("Enter your first number")),(int(input("Enter your second number"))))
    elif choice == 4:
        div(int(input("Enter your first number")),(int(input("Enter your second number"))))
    elif choice == 5:
        square(int(input("Enter the number you want squared.")))
    elif choice == 6:
        squareroot(int(input("Enter the number you want squarerooted.")))
    elif choice == 7:
        cube(int(input("Enter the number you want cubed.")))
    elif choice == 8:
        cuberoot(int(input("Enter the number you want cuberooted")))
    elif choice == 10:
        loop = 0

    time.sleep(3)
"""
    elif choice == 9:
        menu2 ()
"""

print ("")
print ("Thankyou for using the super awesome calculator v0.1")