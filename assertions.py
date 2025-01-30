# Assertions

''' Demonstrate using assertions '''

from math import floor
import py_compile

assert 1 == 1.0, 'The integer 1 should equal the float 1.0'

def round_down(num):
    return floor(num)

assert 6 == round_down(6.999), 'round_down should always round a float down'

try:
    assert -5 == round_down(-5.999), 'round_down should always round a float down'
except AssertionError as exception:
    print('Handled AssertionError:', exception)

try:
    if __debug__:
        if -5 != round_down(-5.999):
            raise AssertionError('round_down should always round a float down')

except AssertionError as exception:
    print('Handled AssertionError:', exception)

print('Assertions are evaluated if __debug__ is True')
print('The value of __debug__ is:', __debug__)
print('Modules executed normally have __debug__ set to True')
print('Modules executed with "python -O" have __debug__ set to False')

if __name__ == '__main__':
    if __file__.endswith('py'): # Only compile when running the source code file
        try:
            py_compile.compile(__file__, __file__ + 'c') # produce .pyc file without optimizing
            py_compile.compile(__file__, __file__ + 'o', optimize=1) # produce .pyo file with optimization
        except Exception as exception:
            print(repr(exception))
