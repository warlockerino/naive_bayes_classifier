class Tokenizer():
	def __init__(self, content):
		self.tokens = {}
		self.stopWords = []
		self.tokenize(content)

	def tokenize(self, content):
		content 	= content.lower()

		content 	= content.replace(".", " ")
		content 	= content.replace(";", " ")
		content 	= content.replace(",", " ")
		content 	= content.replace("/", " ")
		content 	= content.replace(":", " ")
		content 	= content.replace("&", " ")
		content 	= content.replace("|", " ")
		content 	= content.replace("\"", " ")
		content 	= content.replace("-", " ")
		content 	= content.split()

		for t in content:
			if t not in self.stopWords:
				if t not in self.tokens:
					self.tokens[t] = 1
				else: 
					self.tokens[t] += 1
	

	def getTokens(self):
		return self.tokens

	def search(self, term):
		pass 

	def printMap(self):
		print self.tokens		

	def sortTokens(self):
		tmpTokens = {}
		for t in self.tokens:
			if t not in tmpTokens:
				tmpTokens[t] = 1
			else:
				tmpTokens[t] += 1

		self.tokens = tmpTokens

		




