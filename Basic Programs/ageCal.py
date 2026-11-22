# Method - 1 : Basic Age Calculation------------------------------------
# birth_year = int(input("Enter your Year of birth: "))

# current_year = 2026

# age = current_year - birth_year

# print("Your Age  is : ",age)

# Method - 2 : Using datetime (current year)-----------------------------
# import datetime

# birth_year = int(input("Enter your Birth year: "))

# current_year = datetime.datetime.now().year
# age = current_year - birth_year

# print(f"your age is {age}")

# Method - 3 : Accurate Age Calculation ----------------------------------

from datetime import date

birth_day, birth_month, birth_year = map(int, input("Enter you birthday (Ex: 02 11 2006): ").split())

today = date.today()

age = today.year - birth_year

if (today.month, today.day) < (birth_month, birth_day):
    age -=1

print("Your age is :", age)



