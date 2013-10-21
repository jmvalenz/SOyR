# encoding=utf-8
# LEER
# Uno, los comentarios son con un gato
# Dos el error raro que te daba de tener que poner dos veces el 7 erra debido a que nunca cerraba el archi, cada vez que quieras abrirlo
# No basta con escribir encima, pq en memoria puede seguir abierto, so cuando vas a perder la referencia hay que cerrarlo


##Creamos todos los archivos vacios
for i in range (0,20):
    s=str(i)
    s="ram/"+s+".txt"
    archi=open(s,'w')
    archi.close()
for i in range (0,800):
    s=str(i)
    s="disco/"+s+".txt"
    archi=open(s,'w')
    archi.close()
##Incicializamos indices y los archivos disponibles en los archivos 0,1,2,3,4
##Nota: el archivo 0.txt tiene los indices de los otros inodos y comienza
##con las posiciones de archivos disponibles a partir de la linea 5
archi=open('disco/0.txt','a')
archi.write("IN:\n005\n006\n007\nNO:\n")
for i in range(8,177):
    if(i<10):
        d="00"
    elif(i<100):
        d="0"
    else:
        d=""
    if(i==176):
        f=str(i)
        archi.write(d+f)
    else:
        f=str(i)
        archi.write(d+f+"\n")
archi.close()        
archi=open('disco/1.txt','a')
for i in range(177,348):
    if(i<10):
        d="00"
    elif(i<100):
        d="0"
    else:
        d=""
    if(i==347):
        f=str(i)
        archi.write(d+f)
    else:
        f=str(i)
        archi.write(d+f+"\n")
archi.close()       
archi=open('disco/2.txt','a')
for i in range(348,519):
    if(i<10):
        d="00"
    elif(i<100):
        d="0"
    else:
        d=""
    if(i==518):
        f=str(i)
        archi.write(d+f)
    else:
        f=str(i)
        archi.write(d+f+"\n")
archi.close()    
archi=open('disco/3.txt','a')
for i in range(519,690):
    if(i<10):
        d="00"
    elif(i<100):
        d="0"
    else:
        d=""
    if(i==689):
        f=str(i)
        archi.write(d+f)
    else:
        f=str(i)
        archi.write(d+f+"\n")
archi.close()
archi=open('disco/4.txt','a')
for i in range(690,800):
    if(i<10):
        d="00"
    elif(i<100):
        d="0"
    else:
        d=""
    if(i==799):
        f=str(i)
        archi.write(d+f)
    else:
        f=str(i)
        archi.write(d+f+"\n")
archi.close()        
##incicializamos inodos en los archivos 5,6 para contactos 7,8 para mensajes y 9,10 para historial
##Nota: La fila de nombre y la fila de unicación usan 30 bytes cada una.
##en total tenemos 453bytes por el primer archivo y 513 por el segundo.453 + 513 = 966 bytes para cada tipo
##966/3 = 322, finalmente tenemos 322 direcciones posibles para contactos, 322 para mensajes y 322 para historial
archi=open('disco/5.txt','a')
archi.write("contactos\nSOyR/Tarea2/disco\n0\n")
archi.close()
archi=open('disco/6.txt','a')
archi.write("mensajes\nSOyR/Tarea2/disco\n0\n")
archi.close()
archi=open('disco/7.txt','a')
archi.write("historial\nSOyR/Tarea2/disco\n0\n")
archi.close()
