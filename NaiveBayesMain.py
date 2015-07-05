from Class 		import Class
from ClassBank 	import ClassBank
from Trainer 	import Trainer
from Loader 	import Loader

def main():

	c = Class( "Politik", "Das ist der Inhalt der Klasse", 10 )
	print c.getTokenSum()
	print c.getTokenSumIgnoreDuplicates()

	b = ClassBank()
	b.addClass( c )
	
	l = Loader()
	
	t = Trainer( l, b )

if __name__ == "__main__":
    main()