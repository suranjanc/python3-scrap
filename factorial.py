def myFactorial(n):
    while n > 1:
        return n*myFactorial(n-1)
    else:
        return 1 

nos = int(input("Enter the number for which you want to calc factorial : "))
value = myFactorial(nos)
print(value)
