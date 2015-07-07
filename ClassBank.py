from Class 	import Class
from Tokenizer import Tokenizer

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

	def getVocabulary(self):
		t = Tokenizer("");
		for c in self.classes:
			t.tokenize(self.classes[c].contentRaw)
		return t;
