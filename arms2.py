def checkArms(nos):
    lenOfNos=len(str(nos))
    compNos=0
    for i in range(lenOfNos):
        compNos+=int(str(nos)[i])**lenOfNos
    if compNos==nos:
        print("True")
    else:
        print("False")

checkArms(153)