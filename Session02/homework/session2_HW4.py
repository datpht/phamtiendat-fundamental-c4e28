# a)
for i in ["*"]:

    print(i*20, end = '')

# b)
n = int(input("nhap n: "))
for i in ["*"]:

    print(i*n, end = '')

# c)
for i in range(9):
    if i % 2 != 0:
        print("*", end = '')
    elif i % 2 == 0:
        print("x", end = '')

# d)
n = int(input("nhap n: "))
for i in range(n):
    if i % 2 != 0:
        print("*",end = '')
    elif i % 2 == 0:
        print("x", end = '')

# f)
for j in range(3):
    print()        
    for i in range(7):
        print("*",end = '')

# g)
n = int(input("nhap n: "))
m = int(input("nhap m: "))

for j in range (m):
    print()
    for i in range(n):
        print("*",end = '')

        
   
