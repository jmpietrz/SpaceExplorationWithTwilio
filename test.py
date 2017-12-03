from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

import room

app = Flask(__name__)

def createTextMessage(sender, action):
	maps = room.Map("rooms.txt", "items.txt")
	save = open("savefile", "ra")
	savefile = save.readlines()
	position = -1
	count = 0
	for i in savefile:
		if sender == i.split(",,")[0]:
			position = count
		count = count + 1
	if position >= 0:
		maps.position = savefile[count][1]
	else:
		save.write(sender, + ",," + "0\n")

	returnValue = maps.performAction(action)
	save.write(sender, ",," | maps.position + "\n")
	return maps.performAction(action)





@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # Start our TwiML response
	resp = MessagingResponse()
	account_sid = "AC7fd1294880ac928421a5823df2c4e2d6"
	auth_token = "08b348a6ef5d67db668511770d91f563"
	client = Client(account_sid, auth_token)
	#message = client.messages.create(to="+16514916260",

	message = client.messages.list()[-1] 
	returnText = createTextMessage(message.From, TextCommand(message.body))

    # Add a message
	resp.message(returnText)

	return str(resp)

if __name__ == "__main__":

    app.run(debug=True)
