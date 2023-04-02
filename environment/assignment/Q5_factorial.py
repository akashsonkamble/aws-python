# Q5. Find out the factorial of a given number.

number = int(input("Enter the number: "))

answer = 1
for i in range(1, number+1):
    answer *= i

print("The factorial of", number, "is:", answer)