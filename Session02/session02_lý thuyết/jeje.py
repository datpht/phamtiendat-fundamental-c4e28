#yob = int(input("enter your yob: "))

#age = 2019 - yob
#if age < 10:
#    print ("BABY")
#elif 10 < age < 18:
#    print("teenage")
#else:
#    print("adult")
    
from random import randint
x = randint(0,100)
print(x)
if x <= 35:
    print("sunny")
elif 35 < x <= 70:
    print("rainy")
else:
    print("cloudy")



a = int(input("Nhap a: ")) 
b = int(input("nhap b: ")) 
c = int(input("nhap c: "))
Delta = b**2 - 4*a*c 
  
print("Delta = ",Delta) 

if Delta < 0:
    print("No solution")
elif Delta == 0:
    x = -b/a 
    print("phuong trinh co nghiem kep: ",x)
else:
    x1 = 0
    x2 = 0
    x1 = (-b + Delta**0,5)/(2*a)
    x2 = (-b - Delta**0,5)/(2*a)
    print("phuong trinh co nghiem x1 = " + "phuong trinh co nghiem x2 = ", x1,x2)
    


