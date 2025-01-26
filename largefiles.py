# writing Large FIles

''' Demonstrate working with large files '''

from timeit import timeit

def file_iter():
    ''' Processes single line into string in memory '''
    with open('games.txt', mode='r') as text_file:
        with open('out.txt', mode='w') as out_file:
            for line in text_file:
                out_file.write(line)

def file_readlines():
    ''' Processes all lines into list in memory '''
    with open('games.txt', mode='r') as text_file:
        with open('out.txt', mode='w') as out_file:
            lines = text_file.readlines()
            out_file.writelines(lines)

def file_readline():
    ''' Processes one line into string in memory '''
    with open('games.txt', mode='r') as text_file:
        with open('out.txt', mode='w') as out_file:
            while 1:
                line = text_file.readline()
                if not line:
                    break
                else:
                    out_file.write(line)


def file_read():
    ''' Processes all lines into string in memory '''
    with open('games.txt', mode='r') as text_file:
        with open('out.txt', mode='w') as out_file:
            out_file.write(text_file.read())


if __name__ == '__main__':
    print('iterator: %5.3f seconds' % timeit(stmt='file_iter()',
                setup='from __main__ import file_iter', number=10))
    print('readlines() and writelines(): %5.3f seconds' % timeit(stmt='file_readlines()',
                setup='from __main__ import file_readlines', number=10))
    print('readline() and writeline: %5.3f seconds' % timeit(stmt='file_readline()',
                setup='from __main__ import file_readline', number=10))
    print('read() and write(): %5.3f seconds' % timeit(stmt='file_read()',
                setup='from __main__ import file_read', number=10))
