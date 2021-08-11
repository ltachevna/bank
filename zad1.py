import random


answer = int(input("введите число:"))
answer1 = int(input("введите число:"))
total = 0
a = random.randint(1,  21)
d = random.randint(1, 21)
a = int(a)
d = int(d)
if answer + answer1 > a + d:
    total += 1
print(total)








