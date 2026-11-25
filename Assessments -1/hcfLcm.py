num1, num2 = map(int, input("Enter two numbers: ").split())

hcf = 1

for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

lcm = (num1 * num2) //  hcf

print("Highest Common Factor: ",hcf)
print("Lowest Common Multiplier: ",lcm)

lcmm =0

for i in range(max(num1,num2), (num1 * num2) +1):
    if i % num1 == 0 and i % num2 == 0:
        lcmm = i
        break

print("Second Lowest Common Multiplier: ",lcmm)