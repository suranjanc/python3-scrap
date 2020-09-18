while True:
    ccnumber=input("What's your card number: ")
    if ccnumber.isdigit():
        intcc=int(ccnumber)
        break

#while intcc > 0:
#    cclist=list(reversed(str(intcc)))

#Luhn's alogithm
#Step1: Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
#Step2: Add the sum to the sum of the digits that weren’t multiplied by 2.
multSum=0
noMultSum=0
digitsPlace=1
intccIter=intcc
while intccIter>0:
    digit = intccIter % 10
    if digitsPlace % 2 == 0:
        multSum = multSum + (2*digit)
    else:
        noMultSum +=digit 
    digitsPlace+=1
    intccIter //= 10
#print(multSum, noMultSum)

#Step3: If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
totalSum=multSum+noMultSum
#print(totalSum)
if totalSum % 10 == 0:
    print("Its a valid number!")
    #placeholder for type of card
    intccIter2=intcc
    ccNosList= [int(nos) for nos in str(intccIter2)] 
    firstDigit=ccNosList[0]
    firstTwoDigits=int(''.join(map(str,(ccNosList[0:2])))) 
    if firstTwoDigits in [34, 37]:
        print("Amex")
    elif firstTwoDigits in [51, 52, 53, 545, 55]:
        print("MasterCard")
    elif firstDigit == 4:
        print("Visa")
else:
    print("Its fradulent")


