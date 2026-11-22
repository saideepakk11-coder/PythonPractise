num1, num2 = map(int, input("Enter two numbers: ").split())

lcm = 0

for i in range(max(num1,num2), (num1 * num2) + 1):
    if i % num1 ==0 and i % num2 == 0:
        lcm = i
        break
print("LCM:",lcm)