#!/usr/bin/env python3

# display a welcome message
print("The rectangle program")
print()

# get input from the user
length = float(input("Please enter the length:"))
width = float(input("Please enter the width:"))

# calculate miles per gallon
Area = length * width
Area = round(Area)
Perimeter = length * 2 + width * 2
Perimeter = round(Perimeter)           
# format and display the result
print()
print("Area:" , Area)
print("Perimeter:", Perimeter)
print()
print("Bye")


