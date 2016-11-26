import threading

class myThread (threading.Thread):
	def __init__(self, fp):
		threading.Thread.__init__(self)
		self.fp = fp
		
	def run(self):
		while True:
			msg = fp.readline()
			print(msg)