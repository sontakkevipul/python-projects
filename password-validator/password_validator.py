password = input("Enter password: ")

upper = False
lower = False
digit = False
symbol = False

for i in password:
    if i.isupper():
        upper = True
    elif i.islower():
        lower = True
    elif i.isdigit():
        digit = True
    else:
        symbol = True

if 8 <= len(password) <= 15 and digit and lower and upper and symbol:
    print("Password is valid")
else:
    if not digit:
        print("Password doesn't have digit")
    elif not upper:
        print("Password doesn't have at least one upper")
    elif not lower:
        print("Password doesn't have at least one lower")
    else:
        print("Password doesn't have symbol")
