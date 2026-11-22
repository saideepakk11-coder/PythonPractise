# num = int(input("Enter a number to print Right Triangle pattern: "))

num = 5

# for i in range(num):
#     for j in range(i):
#         print("*", end=" ")
#     print()
    
    
#Inverted Right Triganle ----
    
# for i in range(num, 0 , -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Number Right Triangle ----

# for i in range(num):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()

#      Inverted Number

for i in range(num, 0, -1):
    for j in range(i):
        print(j+1, end=" ")
    print()

