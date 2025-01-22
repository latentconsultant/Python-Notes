#command line
'''Accept command line arguements to the module '''

program = 'argv_demo.py'
source = 'default.src'
dest = 'default.dst'

def show_config():
    print('Here is the current configuration:')
    print('Program: %s' % program)
    print('Source: %s' % source)
    print('Destination: %s' % dest)

if __name__=='__main__':
    import sys
    print('Here is sys.argv: %s' % sys.argv)
    if len(sys.argv) > 2: # Two or more arguements passed
        program, source, dest = sys.argv[:3]
    elif len(sys.argv) > 1: # Only one arguement passed
        program, source = sys.argv[:2]
    else: # No arguements passed
        program = sys.argv[0]
    show_config()
