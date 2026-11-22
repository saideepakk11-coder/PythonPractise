num1, num2 = map(int, input("Enter two numbers:").split())
op = input("Enter the operator (+, -, *, /, %): ")

match op:
    case '+':
        print(f" {num1} + {num2} = ",num1+num2)
    case '-':
        print(f" {num1} - {num2} = ",num1-num2)
    case '*':
        print(f" {num1} * {num2} = ",num1*num2)
    case '/':
        if  num2 == 0:
            print("Cannot perform Division with zero!")
        else:
             print(f" {num1} / {num2} = ",num1/num2)
    case '%':
        if num2 == 0:
            print("Cannot perform modulus with zero!")
        else:
            print(f"{num1} % {num2} = {num1 % num2}")
        
