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

#def writeToRam(block , info):
#	print "TODO"

def agregarIndicador(info,indicador):
        lista =[]
        stri = info
        while True:
                num=stri.find("\n")
                if num!=-1:
                        ##print stri[:num]
                        lista.append(stri[:num])
                        stri=stri[(num+1):]
                elif stri!="":
                        lista.append(stri)
                        break
                else:
                        break
        ret=""
        for i in range(0,len(lista)):
                ret=ret+indicador+lista[i]+"\n"
        return ret
        
                

                
def writeToRam(block , info):
        
        if block<20:
        	mitad=0
        	path='ram/'+str(block)+'.txt'
        else:
        	mitad=1
        	path='ram/'+str(block-20)+'.txt'
        w=open(path,'a')
        r=open(path,'r')

        cont1=0
        cont2=0
        archivo=r.readlines()
        for i in range(0,len(archivo)):
                if archivo[i][:2]=="1*":
                        cont1=cont1+len(archivo[i])-2
                elif archivo[i][:2]=="2*":
                        cont2=cont2+len(archivo[i])-2
        if mitad==1:
                if len(info)+cont1<=513:
                        w.write(agregarIndicador(info,"1*"))
        else:
                if len(info)+cont2<=513:
                        w.write(agregarIndicador(info,"2*"))
        r.close()
        w.close()
               

def eraseFromRam(block):
	availableRam.append(block)

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
			info=info+str(c)
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







