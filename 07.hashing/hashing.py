import bcrypt

pw = "Password123"

hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()

given = input('Please enter the password >> ')

if bcrypt.checkpw(given.encode(), hashed.encode()):
    print("That's right!")
else:
    print("That's not it")
