#!/usr/bin/env python

#Import dependencies

import RPi.GPIO as GPIO
import time
import MySQLdb 

#Set db:
db = MySQLdb.connect(host="localhost", user="root", passwd="B@rney9926947!", db="sprinker")

#Set to true to show new results:
db.autocommit(True)

#Set board numbering
GPIO.setmode(GPIO.BOARD)

#Asign names to pins:
Zone1 = 36
Zone2 = 38
Zone3 = 40
Zone4 = 37

#Set up pins as outputs
GPIO.setup(Zone1, GPIO.OUT)
GPIO.setup(Zone2, GPIO.OUT)
GPIO.setup(Zone3, GPIO.OUT)
GPIO.setup(Zone4, GPIO.OUT)

#Set all pins to high as relay board active low
GPIO.output(Zone1, GPIO.HIGH)
GPIO.output(Zone2, GPIO.HIGH)
GPIO.output(Zone3, GPIO.HIGH)
GPIO.output(Zone4, GPIO.HIGH)

#Define Process for switching zones on/off

def SwitchZone(z):
	#Switch all off:
	GPIO.output(Zone1, GPIO.HIGH)
	GPIO.output(Zone2, GPIO.HIGH)
	GPIO.output(Zone3, GPIO.HIGH)
	GPIO.output(Zone4, GPIO.HIGH)
	
	print "Input was: " + z

	#Switch on specific zones:
	if z == "1" :
		print "Turning on zone 1"
		GPIO.output(Zone1, GPIO.LOW)

	if z == "2":
		print "Turning on zone 2"
		GPIO.output(Zone2, GPIO.LOW)
	
	if z == "3":
		print "Turning on zone 3"
		GPIO.output(Zone3, GPIO.LOW)
	
	if z == "4":
		print "Turning on zone 4"
		GPIO.output(Zone4, GPIO.LOW)

def MainPro():
	print "Get active zones ..."
	#Create a cursor for the select
	cur = db.cursor()

	#Run stored procedure
	cur.execute("CALL get_active_zones();")

	#Get all data:
	for row in cur.fetchall() :
		#Get Active Zone number
        	zone = str(row[0])
		print "Active zone should be: " + zone
		#Switch Zones:
		SwitchZone(zone)

	#Close cursor connecton 	
	cur.close()
try:

	var = 1
	while var == 1 :
		print "Looping ..."
		MainPro()
		print "Sleeping ...."
		time.sleep(5)

except KeyboardInterrupt:
	print ""
	print "program quitting ..."

except:
	print "other errors ...."

finally:
	GPIO.cleanup()
	print "BYE"
