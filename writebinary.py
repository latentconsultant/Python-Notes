# Writing binary data

''' Demonstrate writing binary in Python '''
from string import ascii_letters
data = bytes(ascii_letters, 'UTF-8')

with open('letters.bin', mode='wb') as out_file: # write binary
    out_file.write(data)

with open('letters.bin', mode='rb') as in_file: #read binary
    data = in_file.read()

print('Bytes data:', data)
print('String data:', data.decode('UTF-8'))
