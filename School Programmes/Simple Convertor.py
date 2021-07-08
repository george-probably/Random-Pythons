"""
Created by George Chachanidze
Date: 30/10/2012
Purpose: Simple Convertor
"""
import time
def menu():
    print ("Welcome to Simple Unit Convertor Beta 0.1")
    print ("")
    print ("1) Inches to Centimetres")
    print ("2) Centimetres to Inches")
    print ("10) Exit")
    return int(input("Select your choice"))

def intocm(number):
    print (number, "inches are equivalent to",number*2.54,"centimetres")
def cmtoin(number):
    print (number, "centimetres are equivalent to",number*0.393700787,"inches")

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        intocm(int(input("Enter ammount of inches")))
    if choice == 2:
        cmtoin(int(input("Enter ammount of centimetres")))
    if choice == 10:
        loop = 0
    time.sleep(3)

print("")
print("Thankyou for using the Simple Unit Convertor (SUC)")