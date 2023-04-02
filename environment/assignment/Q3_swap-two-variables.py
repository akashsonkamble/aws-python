# Q3. Python program to swap two variables.

firstNumber = 10
secondNumber = 25

firstNumber = firstNumber ^ secondNumber
secondNumber = firstNumber ^ secondNumber
firstNumber = firstNumber ^ secondNumber

print('firstNumber:', firstNumber, 'secondNumber:', secondNumber)