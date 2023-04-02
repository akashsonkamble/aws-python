# Q9. Print 1 to N prime numbers using a while loop.

def is_prime(n):
    if (n == 0 or n == 1):
        return False;
  
    i = 2
    while (i < n):
        if n%i == 0:
            return False
        i += 1
    return True

n = int(input("Enter the number: "))

print("Prime Numbers: ", end=" ")
r=1
while (r <= n):
    if(is_prime(r)):
        print(r, end=" ")
    r+=1