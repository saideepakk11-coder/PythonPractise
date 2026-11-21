num = int(input("Enter a number: "))

originalNum = num
armstrongNumber =0
count = 0

while num > 0:
    num //= 10
    count +=1
    
num = originalNum

while num > 0:
    numm = num % 10
    armstrongNumber += numm ** count
    num //= 10

if originalNum == armstrongNumber:
    print("It is a Armstrong Number")
else:
    print("It is not a Armstrong Number")
    

