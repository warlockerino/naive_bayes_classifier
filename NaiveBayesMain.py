from Class 		import Class
from ClassBank 	import ClassBank
from Trainer 	import Trainer
from Loader 	import Loader

def main():

	c = Class( "Politik", "Das ist der Inhalt der Klasse", 10 )
	d = Class( "Wirtschaft", "Noch eine Geschichte mit Inhalt", 10 )

	b = ClassBank()
	b.addClass( c )
	b.addClass( d )

	b.train()

	classes = b.getClasses()

	for c in classes:
		for t in classes[c].condProb:
			prob = classes[c].condProb
			print t,"=",prob[t]

if __name__ == "__main__":
    main()