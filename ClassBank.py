from Class 	import Class
from Tokenizer import Tokenizer

class ClassBank():
	
	def __init__(self):
		self.classes = {}
		self.tokenizer = Tokenizer("");

	def addClass(self, classInst):
		self.classes[ classInst.getName() ] = classInst
		self.tokenizer.tokenize(classInst.contentRaw)

	def getClass(self, name):
		if name in self.classes:
			return self.classes[ name ]
		return false

	def getClasses(self):
		return self.classes

	def getVocabulary(self):
		return self.tokenizer

	def getVocabularySum(self):
		return len(self.tokenizer.getTokens())

