# num = int(input("Enter a number: "))

# reversedNumber = 0
# num1 = num

# while num > 0:
#     numm = num % 10
#     reversedNumber = reversedNumber * 10 + numm
#     num //= 10
# print(reversedNumber)    
# if num1 == reversedNumber:
#     print("It is a palindrome number")
# else:
#     print("It is not a palindrome number")

num = input("Enter a number: ")

reversedNumber = num[::-1]

if num == reversedNumber:
    print("It is palindrome number")
else:
    print("It is not a palindrome number")