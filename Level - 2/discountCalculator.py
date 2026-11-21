purchase_amount = int(input("Enter Total Purchased Amount: "))

if purchase_amount <=0:
    print("Please Enter Valid Amount !")
else:
    if purchase_amount <1000:
        discount = 0
    elif purchase_amount <=5000:
        discount = 5
    elif purchase_amount <=10000:
        discount = 10
    elif purchase_amount <= 20000:
        discount = 15
    else:
        discount = 20
        
    discount_amount = purchase_amount * discount / 100
    total_bill = purchase_amount - discount_amount

    print(f"Original Amount: {purchase_amount}")
    print(f"Discount: {discount}%")
    print(f"Discount Amount: {discount_amount:.2f}")
    print(f"Final Bill: {total_bill:.2f}")

