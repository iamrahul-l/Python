birthyear = input("Enter your year of birth: ")
if birthyear.isdigit() and int(birthyear) < 2024:
    if len(birthyear) == 2:
        century = input("Please enter the century 19 or 20: ")
        if century == "19" or century == "20":
            userage = (2024-int(century+birthyear))
            print(f"User age is {userage}")
        else:
            print(f"Invalid {century} entered")
    else:
        print(f"The user age is: {2024-int(birthyear)}")
else:
    print(f"The entered year of birth is invalid")            



