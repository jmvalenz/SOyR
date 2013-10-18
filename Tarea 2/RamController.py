from Queue import *
from DiscController import*


availableRam=list()
discToRam={}
savedFIFO=Queue()

def startRam():
	global availableRam
	for i in range(0,40):
		availableRam.append(i)
def readDiscToRam(request):
	global availableRam
	global discToRam
	global savedFIFO

	if len(availableRam)==0:
		aux=savedFIFO.get()
		ramToDisc.pop(aux)
		availableRam.append(aux)

	info=readFromDisc(request)
	print info




startRam()
readDiscToRam(500)

