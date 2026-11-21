num1, num2 = map(int, input("Enter two numbers: ").split())

if num1 > num2 :
    print(f"{num1} is largest number")
elif num2 > num1:
    print(f"{num2} is largest number")
elif num1 == num2:
    print("Both are Equal")
