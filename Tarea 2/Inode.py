# encoding=utf-8

import DiscDriver
import Disc

class Inode(object):
	
	def __init__(self, filename):
		self.filename = filename
		f = DiscDriver.openFile(self.filename)
		#Extraigo metadata.....Definir bien y eliminar simbolos blancos


		self.name = self.CleanName(f.readline())
		
		lines = f.readlines()
		self.available_space_in_last_block = int(lines[1].strip())

		self.blocks = lines[2:]

		f.close()

		#Limpio
		self.blocks=[item.strip() for item in self.blocks]


	def AddNewElement(self, element):
		print "AVAILABLE SPACE ", self.available_space_in_last_block
		if self.available_space_in_last_block <= 0:
			#CREO NUEVO BLOCK Y LO AGREGO A ESTE INODO
			new_block = Disc.getFirstAvailableBlock()
			print "NEW BLOCK", new_block
			if new_block != -1:
				self.blocks.append(new_block)
				DiscDriver.addBlockToFile(self.filename, new_block)
				self.available_space_in_last_block = 513
			else:
				return False

		print self.blocks
		print len(self.blocks)
		DiscDriver.appendToFile(element, self.blocks[-1])
		#CUANTO ES EL TAMAÑO DEL ELEMENTO?!?!?!?!?!?!!
		self.available_space_in_last_block -= 3
		DiscDriver.updateFreeSpaceInInode(self.filename, self.available_space_in_last_block)
		return True

	
	def CleanName(self, line):
		# De 'Nombre: Contactos.txt' retorna 'contactos'
		#return line.split(" ")[1].strip().lower().split(".")[0]

		#NUEVA CONVENCION, el archivo tiene 'contactos' en la primera linea
		return line.strip()