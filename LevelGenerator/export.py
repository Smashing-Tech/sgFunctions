#!/usr/bin/python
"""
Level Generator for Smash Hit

This utility converts a basic description of a level into a .lua file.
"""

import tkinter
import tkinter.ttk as ttk
import json
import os
import sys

def loadJson(infile):
	"""
	Load a JSON file to a string.
	"""
	
	c = None
	
	with open(infile, "r") as f:
		c = json.load(f)
	
	return c

def writeFile(string, outfile):
	"""
	Write a string to a file
	"""
	
	with open(outfile, "w") as f:
		f.write(string)

def exportRoom(string, outfile = None):
	"""
	Export a room to a lua file
	"""
	
	# Load level description
	level = string
	
	# Load level file name
	filename = level["room"] + ".lua.mp3"
	
	if (outfile):
		filename = outfile
	
	# Start creating lua string
	lua = "-- This file was automatically generated. Do not edit it manually.\n\nfunction init()\n"
	
	# Start and end room
	start = level.get("start", None)
	end = level.get("end", None)
	
	if (start or end):
		if (start):
			lua += "\tpStart = mgGetBool(\"start\", true)\n"
		
		if (end):
			lua += "\tpEnd = mgGetBool(\"end\", true)\n"
		
		lua += "\t\n"
	
	# Add music
	lua += "\tmgMusic(\"" + level["music"] + "\")\n"
	
	# Add fog colour
	fog = level["fog"]
	
	lua += "\tmgFogColor(" + str(fog[0][0]) + ", " + str(fog[0][1]) + ", " + str(fog[0][2]) + ", " + str(fog[1][0]) + ", " + str(fog[1][1]) + ", " + str(fog[1][2]) + ")\n\t\n"
	
	# Configure segments
	levelname = level["level"]
	roomname = level["room"]
	
	for segment in level["segments"]:
		lua += f"\tconfSegment(\"{levelname}/{roomname}/{segment}\", 1)\n"
	
	# Register segments
	length = level["length"]
	
	lua += f"\t\n\tlocal accum_length = 0\n\tlocal room_length = {length}\n\t\n"
	
	if (start):
		lua += f"\tif pStart then\n\t\tmgSegment(\"{levelname}/{roomname}/{start}\", -accum_length)\n\tend\n"
	
	lua += """\t\n\twhile accum_length < room_length do
		accum_length = accum_length + mgSegment(nextSegment(), -accum_length)
	end\n\t\n"""
	
	if (end):
		lua += f"\tif pEnd then\n\t\tmgSegment(\"{levelname}/{roomname}/{end}\", -accum_length)\n\tend\n"
	
	# Finish lua
	lua += "\t\n\tmgLength(accum_length)\nend\n\nfunction tick()\nend\n"
	
	# Write file
	writeFile(lua, filename)

def gui():
	window = tkinter.Tk(className = "LevelMaker")
	window.title("Smash Hit Level Maker")
	window.geometry("600x600")
	
	ttk.Frame(window)
	
	input_feild = tkinter.Entry(window, width = 95)
	input_feild.place(x = 10, y = 35)
	
	output_feild = tkinter.Entry(window, width = 95)
	output_feild.place(x = 10, y = 80)
	
	def x(): exportRoom(loadJson(input_feild.get()), output_feild.get())
	
	export_button = tkinter.Button(window, text = "Generate Room", command = x)
	export_button.place(x = 10, y = 110)
	
	window.mainloop()

def main():
	if (sys.argv[1] == "export"):
		exportRoom(loadJson(sys.argv[2]))
	elif (sys.argv[1] == "gui"):
		gui()

if (__name__ == "__main__"):
	main()
