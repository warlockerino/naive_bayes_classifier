import os
from Tokenizer	import Tokenizer
from Classifier import Classifier
from Class 		import Class
from ClassBank 	import ClassBank
from Trainer 	import Trainer
from Loader 	import Loader

def main():


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


if __name__ == "__main__":
    main()