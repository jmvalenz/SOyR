from RamController import*

def getInfo(name):

	info=""
	inode=inodes[name]
	for block in inode.blocks:
		info=info+str(read(block))

	return info

def addInfo(info , name):
	writeToDisc(info , name)

boot()
startRam()