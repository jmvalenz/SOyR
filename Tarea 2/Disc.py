# encoding=utf-8
from Inode import *
import DiscDriver

availableDisc = []
inodes = {}

#Metodo que bootea el sistema operativo, es decir, carga todo lo necesario
def boot():
  global inodes
  global availableDisc
  f = DiscDriver.openIndexFile()
  #Saco la primera linea, solo dice IN: y no es necesaria para nada
  f.readline()

  # Saco la ubicacion de los inodos y los creo, guardandolos en un hash
  for line in f:
    line = line.strip()
    if(line == "NO:"):
      break
    inode=Inode(line)
    inodes[inode.name]=inode       

  #Guardo todos los bloques disponibles
  availableDisc.extend(f)
  f.close()
  for filename in DiscDriver.getIndexFiles():
    f = open(filename)
    availableDisc.extend(f)
    f.close()
  
  #Elimino simbolos blancos para evitar futuros problemas
  availableDisc=[item.strip() for item in availableDisc]

  

def writeContentToDisc(content, content_type):
  global inodes
  inodes[content_type].AddNewElement(content)

def getFirstAvailableBlock():
  global availableDisc
  try:
    return availableDisc.pop(0)
  except IndexError:
    print "Memoria Llena"
    return -1