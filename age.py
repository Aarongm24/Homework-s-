age = int(input("age: "))


if age >= 0 and age <= 12:
    print("child")
    
elif age >= 13 and age <= 17:
    print("teenager")
    
elif age >= 18 and age <=63:
    print("adult")
    
else:
    print("senior")