from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7fd1294880ac928421a5823df2c4e2d6"
# Your Auth Token from twilio.com/console
auth_token  = "08b348a6ef5d67db668511770d91f563"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16514916260", 
    from_="+17632519183",
    body="Hello from Python!")

print(message.sid)
