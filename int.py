x = 5
y = 10
y = 0xA # hexadecimal
y = 0o12 # octal
y = 0b1010 # binary
print('x =', x, ',', 'y =', y)
# Typical comparisons can be made
print('x == y =', x == y)
print('x != y =', x!= y)
print('x >= y =', x >= y)
print('x > y =', x > y)
print('x <= y =', x <= y)
print('x < y =', x < y)
# The usual operators can be used:
print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x < y =', x < y)
# In python 2, x / y uses floor division like:
print('x // y =', x // y) # division
print('x % y =', x % y) # remainder
print('x ** y =', x ** y) # power
# There are several useful builtin functions:
print('divmod(x, y) =', divmod(x, y))# divisor and remainder
print('pow(x, y) =', pow(x,y))# power function
print('abs(-x) =', abs(-x))# absolute value
print('int(5.2) =', int(5.2))# converts data to int
print('int("0xff", 16) =', int("0xff", 16))# integer to floating point
print('float(x) =', float(x))
#Inline notation can also be used:
print('x = x + y =', end = ' ')
x += y
print(x)
print('x = x - y =', end = ' ')
x -= y
print(x)
print('x = x * y =', end = ' ')
x *= y
print(x)
print('x = x / y =', end = ' ')
x /= y
print(x)
# Multiple assignments can be done:
x, y = 4, 2
print('x =', x, ',', 'y =', y)
# Bitwise operators can be used
print('Or: x | y =', x | y)
print('Xor: x ^ y =', x ^ y)
print('And: x & y =', x & y)
print('Left shift: x << y =', x << y)
print('Right shift: x >> y =', x >> y)
print('Inversion: ~x =', ~x)
