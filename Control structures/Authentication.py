age = int(input("age: "))
sex = input("gender: ")

if age >= 18:
    if sex == "male":
        print("YOU'RE A MAN")
    else:
        print("YOU'RE A WOMAN")
else:
    print("YOU'RE A MINOR")
