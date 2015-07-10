from __future__ import division
import math

class Classifier():

	def classify(self, tokens, classbank):
		scores = {}
		currentMax = 0
		currentMaxClass = ""
		for key, c in classbank.getClasses().iteritems():
			scores[key] = math.log10(c.getPrior())
			for term, count in tokens.iteritems():
				if (term in c.condProb):
					scores[key] = scores[key] + (math.log10(c.getCondProb(term)) * count)
			if currentMax == 0:
				currentMax = scores[key]
				currentMaxClass = c.getName()
			if scores[key] > currentMax:
				currentMax = scores[key]
				currentMaxClass = c.getName()
		return classbank.getClass(currentMaxClass)

