from Class 		import Class
from ClassBank 	import ClassBank
from Trainer 	import Trainer

def main():

	c = Class( "Politik" )
	
	b = ClassBank()
	b.addClass( c )
	
	l = Loader()
	
	t = Trainer( l, b )