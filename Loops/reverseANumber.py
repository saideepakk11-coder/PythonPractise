num = int(input("enter a number: "))

#revNum = num[::-1]
revNum = 0

while num > 0:
    numm = num % 10
    revNum = revNum * 10 + numm
    num //= 10

print(revNum)