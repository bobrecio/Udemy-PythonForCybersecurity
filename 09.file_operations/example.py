import json

with open("./credentials.json", "r") as cred_file:
    # creds = cred_file.read()
    data = json.load(cred_file)
    print(type(data))
    cred_file.close()

email_creds = data["email_credentials"]
email = email_creds["email"]
password = email_creds["password"]

print(email, password)
