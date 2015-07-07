
class Classifier():

	def classify(self, tokens, classbank):
		# need for getClasses & getTokens & countTokens
		classes = classbank.getClasses()
		vocab = classbank.getVocab()
		docTokens = tokens
		probIn = 1.0
		bestProb = 0.0
		for c in classes:
			for dt in docTokens:
				probIn *= ((c.getTokenSum()) + 1 ) / (c.getTokens + classbank.getVocab())
			if probIn > bestProb:
				bestProb = probIn
				bestClass = c
		return bestClass
		