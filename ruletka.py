import random

score = dict()

answer = int(input("введите кол-во игроков:"))
name = []
for i in range(answer):
    name.append(input("введите имя:"))
name.sort()
score = dict.fromkeys(name, 0)
print(score)
while True:
    buliet = random.randint(1, 6)
    s = 0
    name = []
    for key in score.keys():
        name.append(key)
    print(name)
    while len(name) > 1:
        for names in name[s:]:
            choice = int(input(names+",крути барабан:"))
            if choice == buliet:
                s = name.index(names)
                print(names+",ты умер")
                name.remove(names)
                score.update({names: score.get(names) + 1})
                buliet = random.randint(1, 6)

                break
            else:
                print("выжил")
        else:
            s = 0
    print(str(name)+", ты победил")
    cont = input("продолжаем?[д,н]")
    if cont.lower == "н":
        break
for key, value in score.items():
    if value == min(score.values()):
        print("больше всех выживал:", key, value)
    if value == max(score.values()):
        print("меньше всех выживал:", key, value)






