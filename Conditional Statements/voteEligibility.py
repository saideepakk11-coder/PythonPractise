age = int(input("Enter your age: "))

if age >= 18 and age <=100:
    print("Congrats, You are Eligible to Vote")
elif age > 1 and age < 18:
    print("Sorry !, You are not eligible to Vote")
else:
    print("Please enter a valid age !")