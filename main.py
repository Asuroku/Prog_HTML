import random


for i in range(20):
    f = open(f"{i}", "w")
    f.write(f'{random.randint(1, 1000)}')
    f.close()