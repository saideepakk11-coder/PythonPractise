num = 5 

for i in range(1, num+1):
    for j in range(num - i):
        print(" ", end=" ")
        
    for k in range(1, i+1):
        print(k, end=" ")
    for k in range(i-1, 0 , -1):
        print(k, end=" ")
    print()