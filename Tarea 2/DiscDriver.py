DISC_LOCATION = "disco/"

def readFromDisc(block): 
	f = open('disco/'+str(int(block))+'.txt')
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

                
# Este metodo asume que content cabe en el archivo a escribir (NO SE LO CUESTIONA)
def appendToFile(content, filename):
        global DISC_LOCATION
        f = open(DISC_LOCATION + str(int(filename)) + '.txt', 'a')
        f.write(content)
        f.close()

def openIndexFile():
        global DISC_LOCATION
        return open(DISC_LOCATION + '0.txt')

def getIndexFiles():
        global DISC_LOCATION
        return [DISC_LOCATION + '1.txt', DISC_LOCATION + '2.txt', DISC_LOCATION + '3.txt', DISC_LOCATION + '4.txt']

def openFile(filename):
        global DISC_LOCATION
        return open(DISC_LOCATION + str(int(filename)) + ".txt")

def addBlockToFile(filename, blocknum):
        global DISC_LOCATION
        appendToFile(blocknum, filename)
        #QUITO DE BLOQUES DISPONIBLES
        removeContentFromFile('000', blocknum)

def updateFreeSpaceInInode(filename, value):
        global DISC_LOCATION
        f = open(DISC_LOCATION + str(int(filename)) + '.txt')
        lines = f.readlines()
        f.close()
        lines[2] = (str(value) + '\n')
        f = open(DISC_LOCATION + str(int(filename)) + '.txt', 'w')
        for line in lines:
                f.write(line)
        f.close()

def removeContentFromFile(filename, content):
        global DISC_LOCATION
        f = open(DISC_LOCATION + str(int(filename)) + '.txt')
        lines = f.readlines()
        f.close()
        lines.remove(str(content) + '\n')
        f = open(DISC_LOCATION + str(int(filename)) + '.txt', 'w')
        for line in lines:
                f.write(line)
        f.close()


#def writeToDisc(info, tipo):##tipo se refiere a si se esta escribiendo un contacto, mensaje o historial
 #       for i in range(0,len(availableDisc)):
  #              u=availableDisc[i][:3]
   #             w=open('disco/'+str(int(u))+'.txt','a')
    #            r=open('disco/'+str(int(u))+'.txt','r')
     #           tipoArchivo=r.readline()
      #          tipoArchivo=tipoArchivo[:-1]
       #         if tipoArchivo=="":
        #                w.write(tipo+"\n")
         #               w.write(info+"\n")
          #              AgregarPunteroAInodo(u,tipo)
           #             return
            #    elif tipoArchivo==tipo:
             #           l=r.readlines()
              #          cont=0
               #         for j in range(0,len(l)):
                #                cont=cont+len(l[j][:-1])
                 #       espacioUsado=len(tipoArchivo)+cont
                  #      if espacioUsado<513:
                   #             w.write(info+"\n")
                    #            return
                     #   else:
                      #          dif=513-espacioUsado
                       #         w.write(info[dif])
                        #        del availableDisc[i]
                         #       writeToDisc(info[dif:],tipo)



        
        


