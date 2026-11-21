num = int(input("Enter a number: "))

if num <= 0:
    print("Factorial is not defined for negative numbers!")
else:
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    print(f"Factorial of {num} is {fact}")