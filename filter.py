# filter function
''' Demonstrate filter function '''
def odd(val):
    return val % 2
nums = range(10)
print('List of nums:', list(nums))
odds = filter(odd, nums)
print('Filter object of odd nums:', odds)
odds = list(filter(odd, nums))
print('List object of odd nums:', odds)
odds = list(filter(lambda val: val % 2, nums))
print('List object of odd nums:', odds)
odds = [val for val in nums if val % 2]
print('List object of odd nums:', odds)

def ncar(val):
    return val.endswith('n')

vehicles = ['sedan', 'coupe', 'hatchback', 'wagon']
ncars = list(filter(ncar, vehicles))
print('List of ncars:', ncars)
ncars = list(filter(lambda val: val.endswith('n'), vehicles))
print('List of ncars:', ncars)
ncars = [car for car in vehicles if car.endswith('n')]
print('List of ncars:', ncars)
        
