time = int(input("time: "))


if time >= 5 and time <= 11:
    print("Morning")
    
elif time >= 12 and time <= 16:
    print("Afternoon")
    
elif time >= 17 and time <=20:
    print("Evening")
elif time >= 21 and time <= 23:
    print("Night")
elif time >= 0 and time <= 4:
    print("Night")
else:
    print("Invalid Time")