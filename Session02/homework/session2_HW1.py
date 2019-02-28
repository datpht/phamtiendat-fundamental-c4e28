print("----------------------------")
print("Chuong trinh Body Mass Index")
print("----------------------------")

weight = int(input("Moi ban nhap can nang: (kg)"))
height = int(input("Moi ban nhap chieu cao: (cm)"))

BMI = float()

BMI = weight / ((height/100)**2)

if BMI < 16:
    print("Extremely underweight")
elif 16 <= BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")