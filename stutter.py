#input the string and add to list
stringList=[ltr for ltr in (input('Please enter the string : ').strip())]
#print(stringList)

#func to stutter
def stutter(strlist):
    repeatstring=''.join(strlist[0:2])
    stutterstring=((repeatstring + "..")*2) + ''.join(item for item in strlist)
    return(stutterstring)

#main
print(stutter(stringList))