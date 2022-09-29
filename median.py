"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        #My solution

        numbers.sort()
        midindex = len(numbers)//2

        print("The median of the list is ", numbers[midindex])


    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
    
print(numbers)
