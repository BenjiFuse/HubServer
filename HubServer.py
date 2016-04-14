#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from datetime import date
from HubController import HubController


app = Flask(__name__)
Controller = HubController()

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/get_door_status")
def get_door_status():
	responseText = Controller.PerformCommand(Controller.CMD_GET_DOOR_STATUS, None)
	return responseText

@app.route("/get_light_status")
def get_light_status():
	return "Light1: out (of the scope of this project)"

@app.route("/get_temperature_status")
def get_temperature_status():
	return "Is it hot in here?"

@app.route("/get_garage_status")
def get_garage_status():
	return "TODO"

@app.route("/authenticate_device")
def authenticate_device():
	return "TODO"

@app.route("/toggle_door$<doorid>")
def toggle_door(doorid):
	log(str(doorid))
	return Controller.PerformCommand(Controller.CMD_TOGGLE_DOOR, doorid)

# Appends the passed message to the current log file
def log(message):
	LogPath = get_current_log_path()
	with open(LogPath, "a") as log_file:
		log_file.write("{}::HubServer::".format(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S') + message + "\n"))

# Returns the full string path of the current log file
def get_current_log_path():
	Today = date.today()
	return "./logs/" + Today.strftime("%Y-%m-%d") + ".log.txt"

# Returns a string containing the current time in "Year-Month-Day Hour:Minute:Second" format
def get_time_string(self):
	return "Current time: " + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
