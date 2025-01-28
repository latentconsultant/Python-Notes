# recursive generators
''' Demonstrate recursive generators '''
def fib_func(n):
    ''' Classic recursive function
    Generate a fibonacci sequence up to n elements
    '''

    if n < 2:
        return n
    return fib_func(n-2) + fib_func(n-1)

func_list = [fib_func(n) for n in range(10)]
print('The func_list of values:', func_list)
func_gen = (fib_func(n) for n in range(10))
print('The func_gen of values:', func_gen)
for n in range(10):
    print('The func_gen value:', next(func_gen))

def fib_gen(n):
    ''' Recursive generator function

    Generate a fibonacci sequence up to n elements
    '''

    element = 0
    f1, f2 = 0, 1
    while element < n:
        yield f1
        f1, f2 = f2, f1 + f2
        element += 1

gen_fib = fib_gen(10)
print('The gen_fib of values:', gen_fib)
for n in range(10):
    print('The gen_fib value:', next(gen_fib))

def fib_inf():
    ''' Recursive generator function

    Generate a fibonacci sequence up to n elements
    '''

    f1, f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

inf_fib = fib_inf()
print('The inf_fib of values:', inf_fib)
for n in range(10):
    print('The inf_fib value:', next(inf_fib))
    
    
