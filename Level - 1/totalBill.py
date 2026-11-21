bill = float(input("Enter Total bill Amount: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (bill * discount)/100
final_bill = bill - discount_amount

print("Discount Amount: ",discount_amount)
print("Final bill: ",final_bill)


