
class Loader():
	def load_txt(self,name):
		file = open(name,'r')
		content = ""
		for line in file:
			content += line
			content += "\n"

		return content
