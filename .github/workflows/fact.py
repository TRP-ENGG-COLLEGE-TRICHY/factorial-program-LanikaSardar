def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input
n = int(input("Enter a number: "))
print(factorial(n))