from random import randint

x = 'hello world!'
for i in range(0,10):
    print(x)
    y = randint(-1,1)
    if y == 1: 
        x = x + 'goodbye world!'
    if y == -1: 
        x = x + 'hello world!'
