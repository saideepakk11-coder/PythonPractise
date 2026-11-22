basicSalary = int(input("Enter your Basic Salary: "))

if basicSalary <=0:
    print("Please Enter Valid Salary!")
else:
    if basicSalary <= 10000:
        HRA_percent = 20
        DA_percent = 10

    else:
        HRA_percent = 25
        DA_percent = 15


HRA = basicSalary * HRA_percent / 100
DA = basicSalary * DA_percent / 100
PF = basicSalary * 12 /100
grossSalary = basicSalary + HRA + DA
netSalary = grossSalary - PF

print(f"House Rent Allowance: {HRA}")
print(f"Dearness Allowance: {DA}")
print(f"Provident Fund: {PF}")
print(f"Gross Salary: {basicSalary} + {HRA} + {DA} = {grossSalary}")
print(f"Net Salary: {grossSalary} - {PF}  = {netSalary}")