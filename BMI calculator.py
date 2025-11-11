Weight = float(input("Enter your wieght in kilogram : "))
Height = float(input("Enter your height in meter : "))

BMI = Weight / (Height ** 2)

if 0 < BMI < 18.5:
    print("Under weight")
elif 18.5 <= BMI <= 24.9:
    print("Normal")
elif 25.0 <= BMI <= 29.9:
    print("Over weight")
elif BMI >= 30:
    print("Obese")
else:
    print("You have entered an invalid input")