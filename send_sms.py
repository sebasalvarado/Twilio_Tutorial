#Download the twilio API
from twilio.rest import TwilioRestClient

#Authentication details
account_sid = "AC52557703c02ac146088bed08255413a4"
auth_token = "10ea554ae8a9441d35cf531f2f9a676a"

client = TwilioRestClient(account_sid, auth_token)
message = client.message.create(to="+593987010622",from_="+19783096210",body="Hola Mami!")
