marks = int(input("Enter your marks: "))

if not 0 <=  marks <= 100:
    print("Please enter valid marks between 0 to 100")
elif  0 <= marks < 35:
    print("You are failed !")
elif marks <= 45:
    print("Just passed")
elif marks <= 55 :
    print("You are passed with D grade")
elif marks <= 70 :
    print("You are passed with C grade")
elif marks <= 85 :
    print("You are passed with B grade")
else:
    print("You are passed with A grade")