# Exceptions Payload

''' Demonstrate raising exception '''

import errno
import os

def check_file(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError # Not recommended

try:
    check_file('invalid.path')
except FileNotFoundError as exception:
    print('#1 Handled FileNotFoundError:', exception)

def check_file_message(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError('"%s" not found' % filepath)

try:
    check_file_message('invalid.path')
except FileNotFoundError as exception:
    print('#2 Handled FileNotFoundError:', exception)

def check_file_args(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(errno.ENOENT,
                                os.strerror(errno.ENOENT),
                                filename,
                                2,
                                'filename2')
try:
    check_file_args('invalid.path')
except FileNotFoundError as exception:
    print('#3 Handled FileNotFoundError:', exception)
    print('Arguments of exception:', exception.args)

def check_file_real(filename):
    f = open(filename)

try:
    check_file_real('invalid.path')
except FileNotFoundError as exception:
    print('#4 Handled FileNotFoundError:', exception)
    print('Arguements of exception:', exception.args)

help(FileNotFoundError)
