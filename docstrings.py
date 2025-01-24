# Docstrings

''' The module docstring appears at top of the file

If a longer description of more that one line is needed,
then a blank line should be skipped after the first line
and then a longer description can be provided.

Blank lines should also be used to seperate multiple
paragraphs as necessary.

PEP 257 defines the technical details of doscstrings.
'''

class DocumentMe():
    ''' The class docstring follows the same rules. '''

    def __init__(self):
        ''' Method docstrings can also be used '''
        self.text = ''' Triple-quoted strings can also be
used to hold WYSIWYG
formatted string.'''

def funk():
    ''' Normal functions should have docstrings too. '''
    pass

''' Docstrings can be used as long comments, as well.'''
print ('The module docstring:', __doc__)
print ('The class docstring:', DocumentMe.__doc__)
print ('A method docstring:', DocumentMe.__init__.__doc__)
print ('A function docstring:', funk.__doc__)
print ('Docstrings are used by Python\'s help function:')
help(__name__)
help(DocumentMe)
help(funk)
    
