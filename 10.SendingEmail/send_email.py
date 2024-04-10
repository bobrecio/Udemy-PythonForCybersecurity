# send an email with the contnent from the API (https://v2.jokeapi.dev/)
# implement logging
# make sure that email creds are not in teh script (external JSON file)
# PROPERLY handle all exceptions specifically


import requests
import json
import smtplib
from email.mime.text import MIMEText

url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

CREDS_FILE = "creds_gmx.json"
# CREDS_FILE = "creds_gmail.json"

with open(CREDS_FILE, "r") as f:
    creds = json.load(f)
    f.close

EMAIL = creds["email"]
PASSWORD = creds["password"]
FROM = EMAIL
RECIPIENT = EMAIL
SMTP = creds["smtp"]
PORT = creds["port"]


def send_email(joke):
    # from: https://mailtrap.io/blog/python-send-email-gmail/
    msg = MIMEText(joke)
    msg["Subject"] = f"Joke from Python"
    msg["From"] = FROM
    msg["To"] = RECIPIENT
    # ---

    s = smtplib.SMTP_SSL(SMTP, PORT)  # use SMTP_SSL
    # s.starttls() # don't use this
    s.login(EMAIL, PASSWORD)
    s.sendmail(FROM, RECIPIENT, msg.as_string())
    s.quit()
    print(f"---\n{msg.as_string()}")


def get_joke_content():
    response = requests.get(url)
    result = response.json()
    if result["error"]:
        return None
    if result["type"] == "twopart":
        setup = result["setup"]
        delivery = result["delivery"]
        return f"Setup: {setup}\nDelivery: {delivery}"
    else:
        joke = result["joke"]
        return f"Joke: {joke}"


joke = get_joke_content()

if joke is not None:
    send_email(joke)
