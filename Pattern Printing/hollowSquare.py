rows = 5

# for i in range(rows):
#     for j in range(i+1):
#         if j == 0 or i == j or i == rows -1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#------------------Inverted----------

# for i in range(rows+1):
#     for j in range(i):
#         if j ==0 or i == rows or i == 0 or j == i -1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows -1 or j == 0 or j == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()