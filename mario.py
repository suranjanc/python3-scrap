while True:
    height=input("What's the height?: ")
    if height.isdigit():
        intheight=int(height)
        if 0<intheight<=8:
            break
        else:
            print("Please enter height b/w 1 and 8")
    else:
        print("Please enter the height in numbers")

for i in range(intheight):
    print(" "*(intheight-1), end="")
    print("#"*(i+1), end="")
    print(" ", end="")
    print("#"*(i+1)) 
    intheight=intheight-1    
    