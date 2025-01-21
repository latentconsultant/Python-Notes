#Python Scripts, Modules, and Programs
'''Provides random greetings

This text file can be used as a Python program, script or module.

'''
import random
sayings = ('Hello', 'Hi', 'Hey', 'Aloha')

def greet():
    return random.choice(sayings)

def test_greet():
    for loop in range(8):
        print(greet(), end=' ')
    print('\ngreetings test completed')

if __name__== '__main__':
    print(greet())
