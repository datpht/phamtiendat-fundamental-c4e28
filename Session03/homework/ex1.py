print("Welcome to our shop, what do you want")
item = ['T-Shirt','Sweater']
print('1. Show item ')
print('2. Add new item ')
print('3. Update position ')
print('4. Delete position ')
print('What do you want ?')

choice = int(input("my choice is "))

while choice != 0:
    if choice == 1:
        print(*item,sep = ', ')
    elif choice == 2:
        i = input('new item: ')
        item.append(i)
        print('your item has been updated')
        print(*item,sep = ', ')
    elif choice == 3:
        i = input('new item: ')
        up = int(input('update positon: '))
        item[up - 1] = i
        print("your position has been updated")
        print(*item,sep = ', ')
    elif choice == 4:
        dp = int(input('Delete position: '))
        del item[dp - 1]
        print("your item has been deleted")
        print(*item,sep = ', ')
    else:
        print("Your choice is not available, please ENTER your choice")

    choice = int(input("my choice is "))