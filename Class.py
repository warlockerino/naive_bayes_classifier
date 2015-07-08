from Tokenizer 	import Tokenizer

class Class():
	
	def __init__(self, name, content, count):
		self.name = name
		self.contentRaw = content
		self.tokens = Tokenizer(content)
		self.condProb = self.tokens.getTokens()
		self.count = count
		self.prior = 0.0

	def setPrior(self, prior):
		self.prior = prior

	def condProbs(self):
		return self.condProb

	def condProb(self, token):
		return self.condProb[token]

	def getName(self):
		return self.name

	def getTokens(self):
		return self.tokens;

	def getTokenSum(self):
		return len(self.tokens.getTokens())

	def getTokenSumIgnoreDuplicates(self):
		count = 0
		for t in self.tokens.getTokens():
			count += self.tokens.getTokens()[t]
		return count