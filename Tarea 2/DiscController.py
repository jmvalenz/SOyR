from boot import*

boot()
def readFromDisc(block): 
	f = open('disco/'+str(block)+'.txt')
	f.readline()
	info=f.readlines()
	f.close()
	info=[item.strip() for item in info]
	return info

def AgregarPuteroAInodo(puntero,tipo):
        if tipo=="contacto":
                inodes["Nombre: Contactos.txt\n"].blocks.append(puntero)
        if tipo=="mensaje":
                inodes["Nombre: Mensajes.txt\n"].blocks.append(puntero)
        if tipo=="historial":
                inodes["Nombre: Historial.txt\n"].blocks.append(puntero)
def writeToDisc(info, tipo):##tipo se refiere a si se esta escribiendo un contacto, mensaje o historial
        boot()
        for i in range(0,len(availableDisc)):
                u=availableDisc[i][:3]
                w=open('disco/'+str(int(u))+'.txt','a')
                r=open('disco/'+str(int(u))+'.txt','r')
                tipoArchivo=r.readline()
                tipoArchivo=tipoArchivo[:-1]
                if tipoArchivo=="":
                        w.write(tipo+"\n")
                        w.write(info+"\n")
                        AgregarPunteroAInodo(u,tipo)
                        return
                elif tipoArchivo==tipo:
                        l=r.readlines()
                        cont=0
                        for j in range(0,len(l)):
                                cont=cont+len(l[j][:-1])
                        espacioUsado=len(tipoArchivo)+cont
                        if espacioUsado<513:
                                w.write(info+"\n")
                                return
                        else:
                                dif=513-espacioUsado
                                w.write(info[dif])
                                del availableDisc[i]
                                writeToDisc(info[dif:],tipo)


