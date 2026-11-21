num = int(input("Enter a number: "))

first = 0
second = 1

print(first, second,end=" ")

for i in range(2,num+1):
    next = first + second
    print(next, end=" ")
    first = second
    second = next