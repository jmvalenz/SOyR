from Inode import *


availableDisc=list()
inodes={}

#Metodo que bootea el sistema operativo, es decir, carga todo lo necesario
def boot():
	global availableDisc
	global inodes
	f = open('disco/0.txt')
	#Saco la primera linea, solo dice IN: y no es necesaria para nada
	f.readline()

	# Saco la ubicacion de los inodos y los creo, guardandolos en un hash
	for line in f:
		line=line.strip()
		if(line=="NO:"):
			break
		inode=Inode(int(line))
		inodes[inode.name]=inode       

	#Guardo todos los bloques disponibles
	availableDisc.extend(f)
	f.close()
	f = open('disco/1.txt')
	availableDisc.extend(f)
	f.close()
	f = open('disco/2.txt')
	availableDisc.extend(f)
	f.close()
	f = open('disco/3.txt')
	availableDisc.extend(f)
	f.close()
	f = open('disco/4.txt')
	availableDisc.extend(f)
	f.close()

	#Elimino simbolos blancos para evitar futuros problemas
	availableDisc=[item.strip() for item in availableDisc]

	


