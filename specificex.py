# Catching specific exceptions

''' Demonstrate handling specific exceptions '''

def specific_handler(x, y):
    print('Calculating %s/%s' % (x,y))
    try:
        z = x / y
    except ZeroDivisionError as exception:
        print('Handled ZeroDivisionError:', exception)
        z = None
    except ArithmeticError as exception:
        print('Handled ZeroDivisionError:', exception)
        z = None
    except TypeError as exception:
        print('Handled TypeError;', exception)
        z = None
    except BaseException as exception:
        print('Unexpected error:'. repr(exception))
    else:
        print('No exception occurred')
        return z
    finally:
        print('Finished specific_handler either way')

if __name__ == '__main__':
    print('Calling specific_handler(5,2) returned:', specific_handler(5,2))
    print('Calling specific_handler(2,0) returned:', specific_handler(2,0))
    print('Calling specific_handler(2,"z") returned:', specific_handler(2,'z'))
    
