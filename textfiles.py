# Read text files # Text file needs to be in same path as .py
''' Demonstrate reading text from a file '''
print('\n************ Iterating over lines ***************')
''' Reading text from a file with default encoding'''
with open('pep20.txt') as text_file:
    for line in text_file:
        print(line, end='')

print('\n********** Using read () method ***********')
''' Reading text from a file with "us" encoding'''
with open('pep20.txt', encoding='us') as text_file:
    text = text_file.read()
print(text)

print('\n********* Using readlines() method ****************')
''' Reading text from a file with "UTF-8" encoding '''
with open('pep20.txt', encoding='UTF-8') as text_file:
    while 1:
        line = text_file.readline()
        if not line:
            break
        else:
            print(line, end='')


print('\n ************ Using error handling ***********')
try:
    ''' Reading text from a file with "UTF-16" encoding '''
    with open('pep20.txt', encoding='UTF-16') as text_file:
        for line in text_file:
            print(line, end=' ')
except UnicodeError:
    print('Problem with Unicode encoding')
