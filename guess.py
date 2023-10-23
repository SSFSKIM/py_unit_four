#Steve
#10.23
import random

a = random.randint(1, 10)
b = int(input('guess the number'))
if a == b:
    print('congratulations!')
else:
    print(f'oh sorry. it was {abs(b-a)} away from the answer: {a}')