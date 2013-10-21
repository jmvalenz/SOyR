from Queue import *
from DiscController import*
from boot import*


availableRam=list()
discToRam={}
savedFIFO=Queue()

def startRam():
	global availableRam
	for i in range(0,40):
		availableRam.append(i)

def writeToRam(block , info):
	print "TODO"
               

def eraseFromRam(block):
	print "TODO"

def read(block):
	if not block in discToRam:
		readDiscToRam(block)

	blockRam=discToRam[block]
	info=""
	if blockRam<20:
		f=open('disco/'+str(blockRam)+'.txt')
		for i in range(0,513):#mal leer los primero 513 hars
			c=f.read(1)
			if not c:
				break
			info=info+str(c)

		f.close()
	else:
		f=open('disco/'+str(blockRam-20)+'.txt')
		for i in range(0,513):
			c=f.read(1)
			if not c:
				break
		for i in range(513,1026):
			c=f.read(1)
			if not c:
				break
			if=info+str(c)
		f.close

	return info	




def readDiscToRam(request):
	global availableRam
	global discToRam
	global savedFIFO

	if len(availableRam)==0:
		aux=savedFIFO.get()
		discToRam.pop(aux)
		availableRam.append(aux)

	info=readFromDisc(request)
	block=availableRam.pop()
	discToRam[request]=block
	writeToRam(block,info)

	print info






