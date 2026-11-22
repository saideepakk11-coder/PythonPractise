num = int(input("Enter a number: "))

originalNum = num

strong = 0

while num > 0:
    fact = 1
    numm = num % 10
    for i in range(1,numm+1):
        fact *= i
    strong +=fact
    num //=10
if strong == originalNum:
    print("It is a Strong number")
else:
    print("It is not a Strong number")