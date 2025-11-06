income = float(input("income: "))

def low():
    print("0%")
def mlow():
    print("15%")
def hlow():
    print("20%")
def middle():
    print("30%")
def high():
    print("35%")

if income >= 0 and income <= 2000:
    low()
elif income >= 2001 and income <= 4000:
    mlow()
elif income >= 4001 and income <= 7000:
    hlow()
elif income >= 7001 and income <= 14000:
    middle()
else:
    high()