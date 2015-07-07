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

	t = b.getVocabulary()
	print t.getTokens()

	print c.getTokenSum()
	print c.getTokenSumIgnoreDuplicates()
	
	l = Loader()
	
	t = Trainer( l, b )

if __name__ == "__main__":
    main()