import os
from twilio.rest import Client

alertMessage = "I NEED A FUCKING GPU2"

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_number = os.environ["TWILIO_NUMBER"]
lcl_number = os.environ["LOCAL_NUMBER"]
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=alertMessage,
         from_= twilio_number,
         to= lcl_number
     )

print(message.sid)