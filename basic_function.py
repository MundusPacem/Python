from math import *

def main():
    radius = input("Enter the radius: ")
    print "main PI: ", pi
    ans = area(radius)
    print "Area of Circle is: ", ans
    print "Value of PI: ", pi

def area(radius):
    pi = 7.5
    print "area of PI: ", pi

    result = pi * pow(radius,2)

    return result

main()

