import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.twilio_acc = os.environ.get("twilio_acc")
        self.twilio_auth = os.environ.get("twilio_auth")
        self.twilio_num = os.environ.get("twilio_num")
        self.my_num = os.environ.get("my_num")

    def send_msg(self, msg):
        client = Client(self.twilio_acc, self.twilio_auth)
        client.messages.create(
            body=msg,
            from_=self.twilio_num,
            to=self.my_num
        )
