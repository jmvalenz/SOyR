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
        
                

                
def writeToRam(info, mitad, path):
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














