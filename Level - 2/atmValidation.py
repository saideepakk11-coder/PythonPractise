withdrawal_amount = int(input("Enter Withdrawal Amount:"))

account_balance = 10000

if withdrawal_amount <=0:
    print("Please Enter Valid Amount !")
else:
    if (withdrawal_amount > account_balance):
        print("Insufficient Balance!")
    elif not (withdrawal_amount % 100 == 0):
        print("Please Enter Amount in Multiplies of 100!")
    else:
        account_balance -= withdrawal_amount
        print("Withdrawal Successful!")
        print(f"Withdrawn Amount: {withdrawal_amount}")
        print(f"Remaining Account Balance: {account_balance}")