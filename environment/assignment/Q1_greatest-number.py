# Q1. Find out the greatest number between three numbers.

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
thirdNumber = int(input("Enter the third number: "))

if firstNumber > secondNumber:
    if firstNumber > thirdNumber:
        print("Greatest Number: ", firstNumber)
    else:
        print("Greatest Number: ", thirdNumber)
else:
    if secondNumber > thirdNumber:
        print("Greatest Number: ", secondNumber)
    else:
        print("Greatest Number: ", thirdNumber)