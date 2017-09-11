#!/usr/bin/env python

#Filename: sprinkler.py
#

import MySQLdb
import time

db = MySQLdb.connect(host="localhost", user="root", passwd="B@rney9926947!", db="sprinker")

db.autocommit(True)

var = 1

while var == 1 :
	#Create a cursor for the select
	cur = db.cursor()

	#Run stored procedure
	cur.execute("CALL get_active_zones();")

	#Display result on screen:
	for row in cur.fetchall() :
        	#Data from rows
        	zone = str(row[0])
        	start = str(row[1])
        	dur = str(row[2])
        	stop = str(row[3])

        	#Print to screen:
        	print "Zone: " + zone
        	print "Start: " + start
        	print "Duration: " + dur
        	print "Stop: " + stop
	cur.close()
	time.sleep(3)
