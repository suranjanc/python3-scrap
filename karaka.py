#vovel dict
voveldict={"a":0, "e":1, "i":2, "o":2, "u":3}
#print(type(str(voveldict['a'])), str(voveldict['a']) )

#get input
strToEncode=input("Pls provide the string you want to encode: ").strip().lower()

#func to implement karaka encoding
def encodeKaraka(strToEncode):
    #Step1: reverse
    reversedStrToEncode=reversed(strToEncode)
    
    #Step2: replace vovels
    encodedAsKaraka=''
    for item in reversedStrToEncode:
        if item in voveldict:
            encodedAsKaraka=encodedAsKaraka + str(voveldict[item])
        else:
            encodedAsKaraka=encodedAsKaraka + item
    
    #Step3: add "aca" suffix
    encodedAsKaraka=encodedAsKaraka + 'aca'
    return encodedAsKaraka

#main
print(encodeKaraka(strToEncode))