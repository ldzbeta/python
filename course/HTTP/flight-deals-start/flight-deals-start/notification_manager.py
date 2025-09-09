from twilio.rest import Client
account_id =""
auth_token =""
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,message):
        self.client = Client(account_id,auth_token)
        self.message = self.client.messages.create(body=message,
    from_="whatsapp:+14155238886",
    to="whatsapp:+15005550006",)
        print(self.message.status)
    