from Class 	import Class

class ClassBank():
	
	def __init__(self):
		self.classes = {}

	def addClass(self, classInst):
		self.classes[ classInst.getName() ] = classInst

	def getClass(self, name):
		if name in self.classes:
			return self.classes[ name ]
		return false

	def getClasses(self):
		return self.classes
