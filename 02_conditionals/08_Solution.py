password = "vaish09@gmail.com"

if len(password) < 6:
    print("Password is weak")
elif len(password) <= 10:
    print("Password is medium")
elif len(password) > 10:
    print("Password is strong")
else:
    print("Invalid password")             