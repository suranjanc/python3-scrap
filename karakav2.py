#vovel dict
vovelDict={"a":0, "e":1, "i":2, "o":2, "u":3}

#get input
strToEncode=input("Pls provide the string you want to encode: ").strip().lower()

#func to implement karaka encoding
def encodeKaraka(strToEncode):
    #Step1: reverse
    reversedStrToEncode=reversed(strToEncode)
    
    #Step2: replace vovels & add "aca"
    encodedAsKaraka=(''.join(str(vovelDict[items]) if items in vovelDict else items for items in reversedStrToEncode))+'aca'

#main
print(encodeKaraka(strToEncode))