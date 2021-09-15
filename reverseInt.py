intToReverse=123456789

print('Reversed using slicing: ', int(str(intToReverse)[::-1]))

print('Reversed using revered: ', int(''.join(reversed(str(intToReverse)))))

newString=''
for i in str(intToReverse):
    newString=i + newString
print('Reversed using for loop: ',newString)