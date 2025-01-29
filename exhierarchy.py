# Exception Hierarchy
''' Demonstrate exception hierarchy '''

from math import exp

def class_hierarchy(class_, space=0):
    print(space * ' ', class_.__name__)
    if not class_ is type:
        for subclass in class_.__subclasses__():
            class_hierarchy(subclass, space + 4)

def math_hierarchy(class_=ArithmeticError, space=8):
    print(space * ' ', class_.__name__)
    for subclass in class_.__subclasses__():
        class_hierarchy(subclass, space + 4)

def overflow_most_specific():
    try:
        z = exp(100000000)
    except OverflowError as exception:
        print('Handling OverflowError:', repr(exception))
    else:
        print('This would print if there was no exception')
    finally:
        print('Most specific handler is deepest in hierarchy')

def overflow_med_specific():
    try:
        z = exp(100000000)
    except ArithmeticError as exception:
        print('Handling ArithmeticError:', repr(exception))
    finally:
        print('Medium specificity handler catches deeper exceptions')

def overflow_least_specific():
    try:
        z = exp(100000000)
    except BaseException as exception:
        print('Handling BaseException:', repr(exception))
    finally:
        print('Least specific exception handles all exceptions')



if __name__ == '__main__':
    class_hierarchy(BaseException)
    #class_hierarchy(object)
    print()
    math_hierarchy()
    print()
    overflow_most_specific()
    print()
    overflow_med_specific()
    print()
    overflow_least_specific()

        
    
