import os
from Tokenizer	import Tokenizer
from Classifier import Classifier
from Class 		import Class
from ClassBank 	import ClassBank
from Trainer 	import Trainer
from Loader 	import Loader
from Tokenizer 	import Tokenizer
from Classifier import Classifier
import glob, os

def main():
	
	folders = {}
	folders["politik"] = "data/politik"
	folders["sport"] = "data/sport"
	folders["wirtschaft"] = "data/wirtschaft"

	bank = ClassBank()
	 
	classes = {}
	
	classes["politik"] = "data/politik/train/"
	classes["wirtschaft"] = "data/wirtschaft/train/"

	for c in classes:
		count = 0
		content = ""

		for file in os.listdir(classes[c]):
			if file.endswith(".txt"):
				l = Loader()
				content += " " + l.load_txt(classes[c] + file)
				count = count + 1

		c = Class(c, content, count)
		bank.addClass(c)

	lo = Loader()

	
	to = Tokenizer(lo.load_txt("data/wirtschaft/test/w011.txt")) 

	classi = Classifier()
	bla = classi.classify(to.getTokenList(), bank)
	print(bla.getName())


	bank = ClassBank()
	l = Loader()

	# train data
	for classname, folder in folders.iteritems():
		count = 0
		content = ""
		for file in os.listdir(folder + "/train/"):
			if file.endswith(".txt"):
				count = count + 1
				content = content + " " + l.load_txt(folder + "/train/" + file)
		c = Class(classname, content, count)
		bank.addClass(c)

 	bank.train()
 	c = Classifier()

 	# test data
 	for classname, folder in folders.iteritems():
 		print "\n=== Testing",classname, "===\n"
		for file in os.listdir(folder + "/test/"):
			if file.endswith(".txt"):
				tokenizer = Tokenizer(l.load_txt(folder + "/test/" + file))
				classifiedClass = c.classify(tokenizer.getTokens(), bank)
				print file,"=",classifiedClass.getName()


if __name__ == "__main__":
    main()