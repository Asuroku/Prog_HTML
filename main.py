import random
import os

summ = 0

for i in range(20):
    f = open(f"BD/{random.randint(850, 950)}", "w")
    f.write(f'{random.randint(1, 1000)}')
    f.close()
for i in os.walk("BD"):
    for j in i[2]:
        f = open(f"BD/{j}", "r")
        a = f.read()
        summ += int(a)
        f.close()
        print(a)
        os.remove(f"BD/{j}")
print(summ)
