num1, num2 = map(int, input("Enter first and second number: ").split())

if num2 == 0:
    print("Cannot check multiples with zero")

if num1 % num2 == 0:
    print(f"{num1} is multiple of {num2} ")
else:
    print(f"{num1} is not  multiple of {num2} ")
