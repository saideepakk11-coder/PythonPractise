marks = int(input("Enter student marks: "))

if 35 <= marks <=100 :
    print(f"Congrats, You passed with {marks} marks")
elif 0 <= marks < 35:
    print("Sorry, you failed! Better luck next time !")
else:
    print("Please enter valid marks between 0 to 100 !")