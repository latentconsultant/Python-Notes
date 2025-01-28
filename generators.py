# Generators 

''' Demonstrate a simple generator '''

def abc_generator():
    yield 'a'
    yield 'b'
    yield 'c'

for char in abc_generator():
    print(char)

def num_generator(num=1):
    while num:
        yield num
        num += 1

for num in num_generator():
    print(num)
    if num == 5:
        break

def doubles(stop=10):
    return (2 * n for n in range(stop))

d_gen = doubles(5)
print('The object d_gen has type:', type(d_gen))
print('The first d_gen number is:', next(d_gen))
print('The second d_gen number is:', d_gen.__next__())

triples = (3 * n for n in range(10))
print('The object triples has type:', type(triples))
print('The first triples number is:', next(triples))
print('The second triples number is:', triples.__next__())
