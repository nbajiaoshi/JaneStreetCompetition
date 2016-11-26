class myThread (threading.Thread):   #继承父类threading.Thread
	def __init__(self, fp):
		threading.Thread.__init__(self)
		self.fp = fp
		
	def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
		while True:
			msg = fp.readline()
			print(msg)