#operator overloading

class Calc():
    ''' Implement basic integer addition operators '''

    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be instantiated with an integer value')
        self.value = value

    def __str__(self):
        '''Define what object returns when str() function is used '''
        return str(self.value)

    def __repr__(self):
        ''' Define what object returns when repr() function is used '''
        return str(self.value)

    def __add__(self, other):
        return self.value + other.value

    def __iadd__(self, value):
        return self.value + value

first = Calc(5)
print('The string of the first object is', str(first))
print('The representation of the first object is', repr(first))
print('__add__ returns the value for first + first:', first + first)
first += 1
print('__iadd__ calculated the value for first +=1:', first)
attrs = dir(first)
print('Other special methods that may be overridden:')
for attr in attrs:
    if attr.startswith('__') and attr.endswith('__'):
        print(attr, end=' ')

