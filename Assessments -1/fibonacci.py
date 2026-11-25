num = int(input("Enter a number: "))

first = 0
second = 1

print(first)
print(second)

for i in range(2,num+1):
    next = first+second
    first = second
    second = next
    print(next)