import csv

#Get the database file and read all values into a Dict. 
csvDictReader = csv.DictReader(open('dna/databases/large.csv'))
dnaDictList=[]
for row in csvDictReader:
    dnaDictList.append(row)

#cast dict value into int
for item in dnaDictList:
    #print(type(item))
    item.update((key,int(value)) for (key,value) in item.items() if key!='name') 
   # dnsDistList2={key:int(value) for (key, value) in item.items() if key!='name'}
#print(dnsDistList2)

#Extract all key for iterating later
dnaDictKey=dnaDictList[0].keys()

#Get the line from the sequence file and get counts for each DNA sequence
seqReader = open('dna/sequences/1.txt')
dnaStr=seqReader.readline()
foundValues={}
for key in dnaDictKey:
    keycount=dnaStr.count(key)
    foundValues[key] = keycount
foundValues.pop('name')
found=False

#Compare the foundValues to the ones in the DB for identifying a match
for dictItem in dnaDictList:
    tempDictItem=dictItem.copy()
    tempDictItem.pop('name')
    if tempDictItem == foundValues:
        print("The DNA matches that of ", dictItem['name'])
        found=True
        break

if found == False:
    print("DNA match not found")