class ClassBank():
	
	def __init__(self):
		self.classes = {}

	def addClass(self, class):
		self.classes[ class.getName() ] = class

	def getClass(self, name):
		if name in self.classes:
			return self.classes[ name ]
		return false

