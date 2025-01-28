# Get Item __getitem__

''' Demonstrate iteration using __getitem__ '''

from random import randint

class LuckyBall():
    ''' Provide an iterable with six random numbers '''

    def __init__(self):
        ''' Generate a list of six unique random integers '''
        self.nums = []
        while len(self.nums) < 6:
            rand_num = randint(1,69)
            if not rand_num in self.nums:
                self.nums.append(rand_num)

    def __getitem__(self, index):
        return self.nums[index]

    def __len__(self):
        return len(self.nums)

if __name__ == '__main__':
    lotto = LuckyBall()
    for num in range(len(lotto)):
        print('The number with index %s is %i' % (num, lotto[num]))

    print('The last number was %i' % lotto[-1])
    print('The first number was %i' % lotto[0])
    print('The second number was %i' % lotto.__getitem__(1))
