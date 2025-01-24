# Documentation best practices
''' Examples for PEP 8, the Style Guide for Python Code

While PEP 8 covers many topics in detail here are some key points:
* Readability counts, as code is read more often than written.
* Following a standard for coding style improves readability.
* Consistency with your code is more important than that with PEP 8,
'''

# each group of imports is seperated by a space
import os # standard library imports should be first
import sys # dont use import os, sys

# import xdb  next, should be related third-party packages installed with pip

# import comments # last, should be local modules
# import doc_strings # do not use wildcard imports


class Layout():
    ''' For each level of indentation four spaces should be used.

    While Python 2 allows the mixing of tabs and spaces, Python 3
    does not. Unless maintaining consistency with existing code,
    only spaces should be used for indentation.

    Lines of text should be limited to maximum of 79 characters.
    Most lines of text, especially comments or documentation should
    be limited to 72 characters. Python allows line wrapping within
    paired delimiters as shown below.
    '''

    @classmethod
    def meaningful_name_of_method(cls,
                                  first_parameter,
                                  second_parameter):
        ''' Use indent that matches opening delimiter.

        For class methods, the first parameter is conventionally named "cls".
        '''
        pass

    def meaningful_method_name(
            first_long_named_parameter,
            second_long_named_parameter,
            third_long_named_parameter):
        ''' Use the same indent for each paramter.

        The indentation can be intended to other than four spaces.
        '''
        pass

    def read_write(self):
        ''' Normal methods conventionally use a first paramter named "self".'''
        with open('/sometimes/the/path/to/the/file/can/be/deep') as file_source, \
             open('/backslash/can/be/used/to/continue/a/single/line', 'w') as file_dest:
                 file_dest.write(file_source.read())

seq_layout_one = (
    'alpha', 'beta',
    'gamma', 'delta'
    )

seq_layout_two = [
    'one', 'two',
    'three', 'four'
]

class NamingConventions():
    ''' General rules for naming Python objects

    Avoid:
    * Single letter names, especially o, O, i, I, l, and L.
    * Meaningless names
    * Names of found in __builtins__
    * Names of packages installed on the system
    '''

    CONSTANT = 24 # Use all uppercase to indicate a "constant" variable.

    def package_and_module(self):
        ''' Module names should be short, all lowercase, and avoid underscores.

        Package names should also be short, all lowercase, and not use underscores.
        '''
        pass

    def class_names(self):
        ''' Class names should use capitalized words, or CapWords, like NamingConventions.

        As Exception objects are also classes, they should also follow this convention,
        but they should have the suffic "Error" added to their name'''
        pass

    def variable_function_method_name(self):
        ''' Variable, function and method names should be all lowercase with underscores.'''
        pass

    def public_or_private(self):
        ''' Public interfaces names should not have leading underscores.

        Private interfaces names should generally have a single leading underscore.
        Names that have two leading underscores will be "mangled" (see PEP 8).
        To avoid clashes with builtin names, use a single trailing underscore.
        '''
        pass
        
