# send an email with the contnent from the API (https://v2.jokeapi.dev/)
# implement logging
# make sure that email creds are not in teh script (external JSON file)
# PROPERLY handle all exceptions specifically


import requests
import json
import smtplib
import logging
from email.mime.text import MIMEText

url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

CREDS_FILE = "creds_gmx.json"
# CREDS_FILE = "creds_gmail.json"

with open(CREDS_FILE, "r") as f:
    creds = json.load(f)
    f.close

LOGFILE = "email_send.log"
EMAIL = creds["email"]
PASSWORD = creds["password"]
SMTP = creds["smtp"]
PORT = creds["port"]
FROM = EMAIL
RECIPIENT = EMAIL

logging.basicConfig(
    filemode="a",
    filename=LOGFILE,
    level=logging.INFO,
    format="%(levelname)s - %(asctime)s - %(message)s",
)


def send_email(joke):
    # from: https://mailtrap.io/blog/python-send-email-gmail/
    msg = MIMEText(joke)
    msg["Subject"] = f"Joke from Python"
    msg["From"] = FROM
    msg["To"] = RECIPIENT
    # ---

    try:
        s = smtplib.SMTP_SSL(SMTP, PORT)  # use SMTP_SSL
    except smtplib.SMTPConnectError:
        logging.error("Could not connect to mail server.")
        exit()

    try:
        s.login(EMAIL, PASSWORD)
    except smtplib.SMTPAuthenticationError:
        logging.error(
            f"Login failed. Did you set the password in the creds file ({CREDS_FILE})"
        )
        exit()

    try:
        s.sendmail(FROM, RECIPIENT, msg.as_string())
    except smtplib.SMTPException:
        logging.error("Could not send email due to error")
        exit()

    s.quit()

    print(f"---\n{msg.as_string()}")


def get_joke_content():
    response = requests.get(url)
    result = response.json()
    if result["error"]:
        logging.error("Something went wrong with the API request")
        return None
    if result["type"] == "twopart":
        setup = result["setup"]
        delivery = result["delivery"]
        return f"Setup: {setup}\nDelivery: {delivery}"
    else:
        joke = result["joke"]
        return f"Joke: {joke}"


joke = get_joke_content()
logging.info("Joke retrieved from API")
if joke is not None:
    send_email(joke)
    logging.info("Joke sent")
