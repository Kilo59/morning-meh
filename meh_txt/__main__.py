import os
from twilio.rest import Client

# Twilio Config
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
FROM_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send(msg):
    return client.messages.create(from_=FROM_NUMBER, body=msg, to=TO_NUMBER)


if __name__ == "__main__":
    print(__doc__)
