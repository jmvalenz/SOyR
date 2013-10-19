
class Inode(object):
	
	#Metadata... Definir bien esto
	blocks=list()
	name=""
	ubication=""

	def __init__(self, path):
		self.ubication=path
		f = open('disco/'+str(path)+".txt")
		#Extraigo metadata.....Definir bien y eliminar simbolos blancos

		self.name=f.readline()
		f.readline()
		f.readline()

		#Agrego los bloques
		self.blocks.extend(f)
		f.close()

		#Limpio
		self.blocks=[item.strip() for item in self.blocks]
