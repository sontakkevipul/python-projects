email = input("Enter your email: ")

username = email.split("@")[0] if "@" in email else ""

if (
    email.count("@") == 1
    and len(username) <= 15
    and "." in email
    and " " not in email
):
    print("Valid email")
else:
    print("Invalid email")
