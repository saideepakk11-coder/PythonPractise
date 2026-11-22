discount_amount = purchase_amount * discount / 100
total_bill = purchase_amount - discount_amount

print(f"Original Amount: {purchase_amount}")
print(f"Discount: {discount}%")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Bill: {total_bill:.2f}")