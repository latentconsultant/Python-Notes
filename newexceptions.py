# creating new exceptions
''' Demonstrate creating a new Exception '''

from time import strftime, localtime

class ProjectBaseError(Exception):
    ''' Base class for all errors in project in project code logs errors '''

    def __init__(self, *args, **kwargs):
        if len(args) > 2 and args[2]:
            logfile = args[2]

        else:
            logfile = __file__ + '.log'

        with open(logfile, mode='a') as logout:
            logout.write(str(strftime('%Ym%d%H%M%S', localtime()) + '\t')) # Year, month, day, hour,minute, second
            logout.write(str(self.__class__) + '\t')
            logout.write(str(args) + '\n')
try:
    raise ProjectBaseError('Demonstrating base class for project')
except ProjectBaseError as exception:
    print('Handling ProjectBaseError:', exception)

class ProjectRequiredValueError(ProjectBaseError):
    ''' An error specific to the project '''

    def __init__(self, message, requested_value, *args):
        self.requested_value = requested_value
        self.message = message
        ProjectBaseError.__init__(self, message, requested_value, *args)

try:
    raise ProjectRequiredValueError('Missing value for first name', 'firstname')
except ProjectRequiredValueError as exception:
    print('Handling ProjectRequiredValueError:', exception.message)
    print('Request value was:', exception.requested_value)

try:
    raise ProjectRequiredValueError('Missing value for last name', 'lastname', 'lastname.log')
except ProjectRequiredValueError as exception:
    print('Handling ProjectRequiredValueError:', exception)
    print('Request value was:', exception.requested_value)
            
                
