class Trainer():
	
	def __init__(self, loader, classBank):
		self.loader = loader
		self.classBank = classBank
		self.results = {}
		self.train()

	def train(self):
		for f in self.loader:
			self.trainSingle(f)

	def trainSingle(self, path):
		classified = Classifier( path, self.classBank )
		self.results[ path ] = classified.getClass()

	def getClass(self, path):
		if path in self.results:
			return self.results[ path ]
		return false
