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