print("WELCOME TO IMPLEMENT WORD JUMBLE GAME")
print(">>>-.-.-.-------------------.-.-.-<<<")
# a) 
letter = ['a','n','m','o','p','h','c','i']
print(*letter)
word = "champion"
loop = True
while loop:
    pw = input("enter the correct word: ")

    if pw == word:
        print("Hura")
        loop = False
    else:
        print(":(")
# b)
letter1 = ['t','s','e','u','m','o','i','u','c','l']
letter2 = ['m','n','c','a','p','i','h','o']
letter3 = ['e','h','x','a','n','g','o']
from random import randint
i = randint(1,3)
if i == 1:
    word1 = "meticulous"
    print(*letter1)
    pw = input('enter the correct word: ')
    if pw == word1:
        print("Hura")
    else:
        print(":(")
if i == 2:
    word2 = "champion"
    print(*letter2)
    pw = input('enter the correct word: ')
    if pw == word2:
        print("Hura")
    else:
        print(":(")
if i == 3:
    word3 = "hexagon"
    print(*letter3)
    pw = input('enter the correct word: ')
    if pw == word3:
        print("Hura")
    else:
        print(":(")

