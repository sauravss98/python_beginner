def createfile():
    for i in range(64,90):
        name=chr(i+1)
        with open(name+".txt",'w') as f:
            f.writelines(name)
createfile()