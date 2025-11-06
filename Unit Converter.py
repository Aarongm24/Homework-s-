print("6. Celicus to Fahrenheit")
print("7. Meter to Feet")

choice = int(input("Enter your choice : "))

def cel_fah(temp):
    print (temp * 9/5 + 32)
def meter_feet(length):
    print (length * 3.280)

if choice == 6:
    tempreature = float(input("tempreature: "))
    cel_fah(tempreature)
elif choice == 7:
    length = float(input("Length: "))
    meter_feet(length)
else:
    print("Unknown option!")






