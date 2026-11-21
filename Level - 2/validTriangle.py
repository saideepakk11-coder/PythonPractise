a, b, c = map(float, input("Enter Trianlge 3 values: ").split())

if a + b > c and a + c > b and b + c > a:
    print("These three sides form a Valid Triangle")
else:
    print("These three sides do not form a Valid Triangle")