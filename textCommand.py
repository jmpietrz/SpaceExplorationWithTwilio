import sys

class TextCommand:
	def __init__(self, message):
		if ("go" in message):
			commandLength = 1
			self.action = "move"
			if ("up" not in message or "down" not in message or "right" not in message or "left" not in message):
				self.action = "invalid"
				commandLength -1
		elif ("investigate" in message or "look at" in message):
			self.action = "investigate"
			if ("look at" in message):
				commandLength = 2
			else:
				commandLength = 1

		elif ("open" in message or "press" in message or "use" in message):
			self.action = "use"
			commandLength = 1

		else:
			self.action = "invalid"
			commandLength = -1

		if (commandLength > 0):
			self.object = " ".join(message.split(" ")[commandLength:])
		else:
			self.object = ""



def main():
	while True:
		text = input("prompt")
		print(text)
		command = TextCommand(text)
		print(command.action)
		print(command.object)
		if (command.action != "invalid"):
			break


if __name__ == "__main__" : main()