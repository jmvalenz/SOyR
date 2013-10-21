from boot import*

boot()
def readFromDisc(block): 
	f = open('disco/'+str(block)+'.txt')
	f.readline()
	info=f.readlines()
	f.close()
	info=[item.strip() for item in info]
	return info

def AgregarPunteroAInodo(puntero,tipo):
        if tipo=="contacto":
                inodes["Nombre: Contactos.txt\n"].blocks.append(puntero)
        if tipo=="mensaje":
                inodes["Nombre: Mensajes.txt\n"].blocks.append(puntero)
        if tipo=="historial":
                inodes["Nombre: Historial.txt\n"].blocks.append(puntero)

def eraseFromDisc(block):
        availableDisc.append(block)

                
def writeToDisc(info, name ):#Me falta lo que hizo felipe, si estoy editando deberia seguir con el bloque anterior y mm que pasa si la info requiere mas de un bloque?
        if len(availableDisc)>0:
                block=availableDisc.pop()
                f = open('disco/'+str(block)+'.txt', 'w')
                f.write(info)
                f.close()

        else:
                print "Memory is full, imposible to save"    


