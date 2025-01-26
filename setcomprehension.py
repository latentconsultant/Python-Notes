# set comprehension

from math import pi
pi_limits = {val * pi * 0.1 for val in range(-10, 11)}
print('pi_limits:', pi_limits)
print('pi in pi_limits:', pi in pi_limits)

from calendar import isleap
leapyears = {year for year in range(2016, 2066) if isleap(year)}
print('leapyears:', leapyears)
print('2016 in leapyears:', 2016 in leapyears)

basket_a = {'apple', 'orange', 'pear'}
basket_b = {'lemon', 'pear', 'peach'}
basket = {fruit_a + fruit_b for fruit_a, fruit_b in zip(basket_a, basket_b) if fruit_a != fruit_b}
print('basket:', basket)
