from Class 	import Class
from Tokenizer import Tokenizer

class ClassBank():
	
	def __init__(self):
		self.classes = {}
		self.documentCount = 0
		self.tokenizer = Tokenizer("");

	def addClass(self, classInst):
		self.classes[ classInst.getName() ] = classInst
		self.tokenizer.tokenize(classInst.contentRaw)
		self.documentCount = self.documentCount + classInst.count

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

	def train(self):
		v = self.getVocabulary().getTokens()
		n = self.documentCount
		for c in self.classes:
			c = self.classes[c]
			c.setPrior(c.count/n)
			t = c.getTokens().getTokens()
			for key in c.condProb:
				c.condProb[key] = (float) (t[key] + 1) / (len(t) + v[key])


