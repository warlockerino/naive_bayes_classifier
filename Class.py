from Tokenizer 	import Tokenizer
class Class():

	def __init__(self, name, content, count):
		self.name = name
		self.contentRaw = content
		self.tokens = Tokenizer(content);
		self.count = count

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
