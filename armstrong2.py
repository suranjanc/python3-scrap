def check_armstrong(nos):
    list_of_nos=[str(i) for i in str(nos)]
    sum_of_nos=0
    for i in list_of_nos:
        sum_of_nos+=int(i)**len(list_of_nos)
    if sum_of_nos==nos:
        return True
    else:
        return False



check_armstrong(10)