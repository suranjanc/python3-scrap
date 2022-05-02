def gen_fib_series(nos):
    fib_list=[]
    for i in range(0,nos):
        if i==0:
            fib_list.append(i)
        elif i==1:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[i-2]+fib_list[i-1])
    return(fib_list) 

#find the 1st X fib numbers
def fib_nos():
    list_of_fib_nos=gen_fib_series(int(input('Generate how many fibnocci series: ')))
    print(*list_of_fib_nos, sep=", ")

fib_nos()