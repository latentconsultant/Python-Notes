# import example
''' Provides random greetings '''
import random
sayings = ('Hello', 'Hi', 'Alo', 'Aloha')

def greet():
    return random.choice(sayings)
