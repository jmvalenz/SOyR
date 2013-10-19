from boot import*

def readFromDisc(block): 
	f = open('disco/'+str(block)+'.txt')
	info=f.readlines()
	f.close()
	info=[item.strip() for item in info]
	return info

boot()