# Lazy Generators

''' Demonstrate lazy generators '''

pi = 3.141592653589793 # from math import pi

print('Create values in memory instead of lazy evaluation')
def numbers(stop=10):
    num_list = []
    for n in range(1, stop + 1):
        print('Adding %s to the num_list' % n)
        num_list.append(n)
    return num_list

def area_circle(radius):
    area = pi * radius ** 2
    print('Circle area with radius %s is: %s' % (radius, area))
    return area

num_list = numbers()
area_list = [area_circle(n) for n in num_list]
print('The list of areas is:', area_list)
num_list = numbers(100)
area_list = [area_circle(n) for n in num_list]
print('The list of areas is:', area_list)

print('\nCreate values with lazy evaluation')

def numbers_gen(stop=10):
    n = 1
    while n < stop + 1:
        print('Yielding n as: %s' % n)
        yield n
        n += 1

def area_circle_gen(radius):
    area = pi * radius ** 2
    print('Circle area with radius %s is: %s' % (radius, area))
    yield area

area_list_gen = (area_circle_gen(n) for n in numbers_gen())
print('The area_list_gen is of type:', type(area_list_gen))
print('Values are generated on demand:')
for area in area_list_gen:
    print(next(area))

a_list = list(area_list_gen)
print('Once used generators no longer produce results:', a_list)
print('Prior to first generation of generator')
area_list_gen = (area_circle_gen(n) for n in numbers_gen())
print('Prior to generation of list of generators')
area_list_gen2 = [n for n in area_list_gen]
print('The area_list_gen2 is of type:', type(area_list_gen2))
print('The contents of area_list_gen2 is:', area_list_gen2)
print('Prior to generation of list of area')
area_list_gen3 = [next(area) for area in area_list_gen2]
print('The area_list_gen3 list of areas is:', area_list_gen3)



