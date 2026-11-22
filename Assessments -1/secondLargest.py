num1, num2, num3 = map(int, input("Enter three numbers: ").split())

if num1 <= num2 <= num3 or num3 <= num2 <= num1:
    print(f"{num2} is Second Largest Number")
elif num2 <= num1 <= num3 or num2 <= num1 <= num3:
    print(f"{num1} is Second Largest Number")
elif num2 <= num3 <= num1 or num2 <= num3 <= num1:
    print(f"{num3} is Second Largest Number")


