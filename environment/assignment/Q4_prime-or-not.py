# Q4. Given number is prime or not.

n = int(input("Enter the number: "))

count = 2;
if n > 1:
    for i in range(2, (n//2)+1):
        if n%i == 0:
            count += 1

if count > 2 or n == 0 or n == 1:
    print("This is not a prime number")
else:
    print("This is a prime number")