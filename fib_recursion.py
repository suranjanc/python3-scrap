listFibs=[0,1]

def gen_fib(nos):
    lenOflist=len(listFibs)
    if nos == 0:
        return 
    else:
        listFibs.append(listFibs[lenOflist-1]+listFibs[lenOflist-2])
        gen_fib(nos-1)

def build_fib_list():
    gen_fib(int(input('How many fib nos?: ')))
    print(*listFibs, sep=', ')

build_fib_list()
