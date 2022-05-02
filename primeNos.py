def check_prime(nos):
    if nos ==1:
        return False
    for i in range(2,nos):
        if nos % i == 0:
            return True
        else:
            return False

def get_number_to_check():
    nosToCheck=int(input("Provide a no to check for prime: "))
    if(check_prime(nosToCheck)):
        print("It's not")
    else:
        print("its Prime!")

get_number_to_check()