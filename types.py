#classes and types

''' Python classes are all types.

The builtin classes have their own types.
User-defined classes can inherit their type
from the builtin classes or the generic type.

The type function can display the type of an object.
The type function can also define a new type.
The class statement is typically used to define a new type.
'''

print('The type of 1 is:', type(1))
print('The type of [] is:', type([]))

A_class = type('A_class', (), {})
print('The type of A_class is:', type(A_class))
an_inst = A_class()
print('The type of an_inst is:', type(an_inst))

A_type = type('A_type', (), {'start':1, 'a_method':
                             lambda self: 'This is an instance of ' +
                             str(self.__class__)})
type_inst = A_type()
print('The type of A_type is:', type(A_type))
print('The type of type_inst is:', type(type_inst))
print('Calling a_method returns:', type_inst.a_method())

class Basic():
    start = 1

    def a_method(self):
        return 'This is an instance of ' + str(self.__class__)

basic_inst = Basic()

print('The type of Basic is:', type(Basic))
print('The type of basic_inst is:', type(basic_inst))
print('Callling a_method returns:', basic_inst.a_method())

