from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7fd1294880ac928421a5823df2c4e2d6"
# Your Auth Token from twilio.com/console
auth_token  = "08b348a6ef5d67db668511770d91f563"

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
