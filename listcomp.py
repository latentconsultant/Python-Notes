# list comprehensions
''' Demonstrate basic list comprehensions '''
# Without list comprehensions:
odds = []
for num in range(10):
    if num % 2:
        odds.append(num)
print('Odd numbers:', odds)

# With a list comprehension
odds = [num for num in range(10) if num % 2]
print('Odd numbers:', odds)

# More examples
nums = [str(num) for num in range(10)]
print('Number strings:', nums)

evens = [num for num in nums if not int(num) % 2]
print('Even numbers:', evens)

alphabet = [chr(ordinal) for ordinal in range(ord('A'), ord('z') + 1) if chr(ordinal).isalpha()]
print('Alphabet:', alphabet)
