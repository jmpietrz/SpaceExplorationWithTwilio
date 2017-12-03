#!/usr/bin/env python

import string

class Room:
	def __init__(self, items, id, description, up, right, down, left, objects):
		self.id = id
		self.description = description
		self.up = up
		self.adjoiningRooms = [up, right, down, left]
		self.objects = objects

		self.items = []

		for i in items:
			for j in objects:
				if i.id == j and j not in self.items:
					self.items.append(i)

	def goDirection(self, direction):
		index = -1
		if direction == "north":
			index = 0
		elif direction == "east":
			index = 1
		elif direction == "south":
			index = 2
		elif direction == "west":
			index = 3
		if index == -1:
			return -1
		return self.adjoiningRooms[index]

class Item:
	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

class Map:
	def __init__(self, roomsFileName = "rooms.txt", itemsFileName = "items.txt"):
		self.position = 0
		itemsFile = open(itemsFileName, "r")
		itemsContents = itemsFile.readlines()
		items = []
		for i in itemsContents:
			items.append(Item(i[0], i[1], i[2]))

		roomsFile = open(roomsFileName, "r")
		roomsContent = roomsFile.readlines()
		self.rooms = []
		for i in roomsContent:
			roomsText = i.split(",,")
			self.rooms.append(Room(items, roomsText[0], roomsText[1], roomsText[2], roomsText[3],
				roomsText[4], roomsText[5], roomsText[6]))

if __name__ == "__main__":
    maps = Map("rooms.txt", "items.txt")
    for i in maps.rooms:
    	print(i.description)
    print("Going up in room 1: " + str(maps.rooms[0].goDirection("north")))
    print("Going right in room 1: " + str(maps.rooms[0].goDirection("east")))
    print("Going down in room 1: " + str(maps.rooms[0].goDirection("south")))
    print("Going left in room 1: " + str(maps.rooms[0].goDirection("west")))
    for i in maps.rooms[0].adjoiningRooms:
    	print(str(i))
