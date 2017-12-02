class Room:
	def __init__(self, id, description, up, right, down, left, objects):
		self.id = id
		self.description = description
		self.up = up
		self.adjoiningRooms = [up, right, down, left]
		self.objects = objects

	def goDirection(self, direction):
		goInDirection = -1
		if (direction == "up"):
			goInDirection = 0
		elif (direction == "right"):
			goInDirection == 1
		elif (direction == "down"):
			goInDirection == 2
		elif (direction == "left"):
			goInDirection = 3
		return goInDirection


class Map:
	def __init__(roomsFileName = "rooms.txt", itemsFileName = "items.txt"):
		self.position = 0
		roomsFile = open(roomsFileName, "r")
		roomsContent = roomsFile.readlines()
		for (i in roomsContent):
			roomsText = i.split(",,")
			self.rooms.append(Room(roomsText[0], roomsText[1], roomsText[2], roomsText[3],
				roomsText[4], roomsText[5], roomsText[6]))

if __name__ == "__main__":
    room = Room(0, "Yo this room is lit", 1, -1, -1, 3, 3)
    room.goDirection("up")
    room.goDirection("right")