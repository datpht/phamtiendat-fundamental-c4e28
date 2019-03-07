choice = {
    'quest1':[35,36,40,44],
    'quest2':['About 55','About 65','About 75','About 85']
}
correct_ans = 0

print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x + 3) ?")

for index,ans in enumerate(choice['quest1']):
    print(index + 1,ans,sep = '. ')

i = int(input("Your choice: "))

if i == 4:
    print("Bingo")
    correct_ans += 1
elif i >= 5:
    print("There are no 5 in the answer")
else:
    print(":(")

print("Estimate this answer (exact calcularion not needed)")
print("Jack score these marks in 5 math tests: 49, 81, 72, 66 and 52.What is the mean")  

for index,ans in enumerate(choice['quest2']):
    print(index + 1,ans,sep = '. ')

i = int(input("Your choice: "))

if i == 2:
    print("Bingo")
    correct_ans += 1
elif i >= 5:
    print("There are no 5 in the answer")
else:
    print(":(")

print("You answered correctly",correct_ans,"out of 2 question")