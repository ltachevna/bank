import random

count = int(input("введите количество чисел:"))
number = input("введите число, кторое будут искать:")
total = 0
for i in range(count):
    compare = random.randint(1, 100)
    total += str(compare).count(number)
print(total)