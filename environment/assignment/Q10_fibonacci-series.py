# Q10. Fibonacci series by using python (first 25 numbers)

n1, n2 = 0, 1
print("Fibonacci Series: ", end=" ")
print(n1, n2, end=" ")
for i in range(2, 25):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3