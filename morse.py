#Get str into a list
strToEncode=[str.upper() for str in input('Please enter the string that you want to encode : ')]
#print(strToEncode)

# the ref dict
char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

#print(char_to_dots[strToEncode[0].upper()])

#func to encode
def encodeMorse(strList):
    morseEncodedStrList=[]
    for item in strList:
        morseEncodedStrList.append(char_to_dots[item])
        morseEncodedStr = ''.join(item for item in morseEncodedStrList)
    return morseEncodedStr

#main 
print(encodeMorse(strToEncode))
