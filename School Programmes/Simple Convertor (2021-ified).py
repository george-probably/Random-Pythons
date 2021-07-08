"""
Created by George Chachanidze
Date: 08/07/2021
Purpose: Simple Convertor (but less bad)
"""
import time
int_rounding = 3
def menu():
    print ("Welcome to Simple Unit Convertor Beta 0.21")
    print ("")
    print ("1) Inches to Centimetres")
    print ("2) Centimetres to Inches")
    print ("5) Change Accuracy")
    print ("10) Exit\n")
    return int(input("Select your choice: "))


def intocm(number):
    print ("\n",number, "inches are equivalent to",round(number*2.54,int_rounding),"centimetres\n")
def cmtoin(number):
    print ("\n",number, "centimetres are equivalent to",round(number*0.393700787,int_rounding),"inches\n",)

loop = 1
choice = 0
while loop == 1:
    try:
        choice = menu()
    except ValueError:
        print("\nWait a second, we're looking for a whole number! Try again...")
    if choice == 1:
        try:
            intocm(float(input("Enter amount of inches: ")))
        except ValueError:
            print("\nWait a second, we're looking for a number! Try again...")
        time.sleep(3)
    if choice == 2:
        try:
            cmtoin(float(input("Enter amount of centimetres: ")))
        except ValueError:
            print("\nWait a second, we're looking for a number! Try again...")
        time.sleep(3)
    if choice == 5:
        try:
            int_rounding = int(input("Enter number of points: "))
        except ValueError:
            print("\nWait a second, we're looking for a whole number! Try again...")
        time.sleep(3)
    if choice == 10:
        loop = 0
    else:
        print("\nThat number is not an option, try again...")

print("")
print("Thank you for using the Simple Unit Convertor (SUC)")
