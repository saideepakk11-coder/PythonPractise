ch = input("Enter a string: ")

chh = ch.upper()
count = 0

while ch == "":
    num = ch % 10
    if ('A' or 'E'or 'I'or 'O' or 'U') == num:
        count +=1


# if ('A' or 'E'or 'I'or 'O' or 'U') in chh:
#     count +=1
    
print("Total Vowels in the String: ",count)
    