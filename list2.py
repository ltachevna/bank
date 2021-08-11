#square = [i*i for i in range(20)]
#print(square)

#a = [i*j for i in range(11) for j in range(11)]
#0print(a)


import random
total = 0
while True:
    answer = input("введите слово(орёл, решка)0 - для выхода:")
    if answer == "орёл" or answer == "решка":
         a = random.choice('орёл')
         d = random.choice('решка')
         if answer == a or answer == d:
             total += 1
    elif answer == "0":
        print(total)
        break






