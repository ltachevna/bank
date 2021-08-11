import random


while True:
    game = input("в нашей программе предоставлено 3 игры: 1. Камень ножницы бумага, 2. Угадай число, 3.Самый часто повторяющийся символ. В какую желаете сыграть(4 - выход из программы)")
    if game == "1":
        c = input("что вы выберете?")
        a = random.choice(["камень", "ножницы", "бумага"])
        if c == "ножницы" and a == "бумага":
            print("вы выиграли")
        elif c == "ножницы" and a == "камень":
            print("вы проиграли")
        elif c == "ножницы" and a == "ножницы":
            print("ничья")
        elif c ==  "бумага" and a == "ножницы":
            print("вы проиграли")
        elif c == "бумага" and a == "бумага":
            print("ничья")
        elif c == "бумага" and a == "камень":
            print("вы выиграли")
        elif c == "ножницы" and a == "бумага":
            print("вы выиграли")
        elif c == "камень" and a == "бумага":
            print("вы проиграли")
        elif c == "камень" and a == "ножницы":
            print("вы выиграли")
        elif c == "камень" and a == "камень":
            print("ничья")
        else:
            print("не знаю таких функций")
            break
    elif game == "2":
        while True:
            print("угадываем")
            min = input("введите минимум ")
            max = input("введите максимум")
            a = random.randint(int(min), int(max))
            while True:
                choice = input("угадай число")
                if int(choice) > a:
                    print("меньше")
                elif int(choice) < a:
                    print("больше")
                else:
                    print("угадали")
                    break
            answer = input("хотите ещё?")
            if answer == "нет":
                break
            else:
                pass
    elif game == "3":
        while True:
            hel = input("введите строку:")
            max = 0
            index = -1
            for sing in hel:
                a = hel.count(sing)
                if a > max:
                    max = a
                    index = hel.index(sing)
                    print(hel[index], max)
    elif game == "4":
        break











