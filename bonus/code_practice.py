import random

lower = int(input('Enter a lower bound: '))
upper = int(input('Enter an upper bound: '))

rand_num = random.randint(lower, upper)
print(rand_num)