from __future__ import division
from Class 	import Class
from Tokenizer import Tokenizer

class ClassBank():

	def __init__(self):
		self.classes = {}
		self.documentCount = 0
		self.tokenizer = Tokenizer("");

	def addClass(self, classInst):
		self.classes[classInst.getName()] = classInst
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
			tCount = 0
			for tKey, tValue in t.iteritems():
				tCount = tCount + (tValue + 1)
			for key, value in v.iteritems():
				vCount = 0
				if key in t:
					vCount = t[key]
				c.condProb[key] = (vCount + 1)/(tCount + len(v))

