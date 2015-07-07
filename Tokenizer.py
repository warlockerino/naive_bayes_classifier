class Tokenizer():
	def __init__(self, content):
		self.tokens = {}
		self.stopWords = ['d01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07', 'd08',  
'a', 'also', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do',
'for', 'have', 'is', 'in', 'it', 'of', 'or', 'see', 'so',
'that', 'the', 'this', 'to', 'we']
		self.tokenize(content)

	# ADD URL ELEMENT TO UPDATE ITS TOKENS
	def tokenize(self, content):
		content 		= content.lower()

		# Replacing all kinds of symbols with whitespace
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

		




