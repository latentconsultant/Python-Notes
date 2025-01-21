# while loop
# The while loop executes a suite of code if its condition is True
# while loop can be used for sequence
counter = 3
while counter > 0:
    print("Counting down:", counter)
    counter -= 1

while 1:
    print('Executes at least once')
    if not counter:
        break

names = ['Tom', 'Ellen']
while names:
    print(names.pop(), 'is going')

results = [1, 0, 1]
processed = 0
passed = 0
while results:
    processed += 1
    result = results.pop()
    if not result:
        continue
    passed += 1
else:
    print('Processed:', processed, 'Passed:', passed)
