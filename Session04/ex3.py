
print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x + 3) ?")
print("1. 35")
print("2. 36")
print("3. 40")
print("4. 44")
i = int(input("Your choice: "))
while i != 0:
    if i == 4:
        print("Bingo")
        break
    elif i >= 5:
        print("There are no 5 in the answer")
    else:
        print(":(")
    i = int(input("Your choice: "))
