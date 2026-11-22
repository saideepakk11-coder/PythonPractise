units = float(input("Enter how many units consumed: "))

if units <=0:
    print("Please enter valid units")

if units <=100:
    bill = units * 1.50
    print(f"Electricity bill: {bill:.2f}")
elif units <=200:
    bill = (units * 1.50) + ((units - 100) * 2.50)
    print(f"Electricity bill: {bill:.2f}")
elif units <= 300:
    bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4)
    print(f"Electricity bill: {bill:.2f}")
else:
    bill = (100 * 1.50) + (100 * 2.50) + (100 * 4) + ((units - 300) * 6)
    print(f"Electricity bill: {bill:.2f}")



    