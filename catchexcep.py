# catching all exceptions

''' Demonstrate handling all errors '''

def all_far(x, y):
    ''' Demonstrate error handling when calling functions '''
    z = x/y
    return z

def all_close(x, y):
    ''' Demonstrate handling all errors within a function '''
    try:
        print('Calculating %s/%s' % (x,y))
        z = x/y
    except BaseException as exception:
        print('Unexpected error->', str(exception))
        print('Unexpected error->', repr(exception))
    else:
        print('No exception occurred')
        return z
    finally:
        print('Finished all_close either way')

if __name__ == '__main__':
    print('Calling all_close(5,2) returned:', all_close(5,2))
    print()
    print('Calling all_close(2,0) returned:', all_close(2,0))
    print()

    ''' Use error handling for calling function all_far() '''
    print('Calling all_far(5,2):')
    z = None
    try:
        z = all_far(5,2)
    except:
        print('Unexpected error!')
    else:
        print('No exception occurred')
    finally:
        print('Finished all_far either way')
    print('Calling all_far(5,2) returned:', z)
    print()

    print('Calling all_far(5,0):')
    z = None
    try:
        z = all_far(5,0)
    except BaseException as exception:
        print('Unexpected error:', repr(exception))
    else:
        print('No exception occurred')
    finally:
        print('Finished all_far either way')
    print('Calling all_far(5,0) returned:', z)
    print()

''' Without error handling, then the following occurs '''
print('Calling all_far(0,z) without error handling:')
z = all_far(0,'z')
print('This will not print because the program has stopped')
print('Calling all_far(0,z) returned:', z)
    
        
