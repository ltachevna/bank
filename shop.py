import os
os.device_encoding(1251)


print("здравствуйте, вы попали в магазин, готовых работ")
GOODS = ["Диплом", "Курсовая", "Практическая"]
KINDS = ["Обычная","С пояснением", "С чертежами"]
COST = [200, 50, 10]
MULTIPLIERS = [1, 1.5, 2]
while True:
    menu = input("вы желаете сделать заказ или наши услуги вас не интересуют?(0 - для выхода)\n" + str(GOODS) + "\nВаш выбор:")
    if menu in GOODS:
        while True:
            hel = input("какой вид работы вас интересует" + menu + ":\n" + str(KINDS) + "\nВаш выбор:")
            if hel in KINDS:
               count = input("Сколько" + menu + "вам надо?")
               count = int(count)
               pay = COST[KINDS.index(hel)] * count * MULTIPLIERS[KINDS.index(hel)]
               while True:
                   answer = input("Стоимость вашей покупки:" + str(pay) + "$\nБудете брать?[y/n]")
                   if answer == "y" or answer == "Y":
                       print("Чек:\nКуплено:" + menu + "\nВ количестве:" + str(count) + "\nСтоимость:" + str(pay) + "\nСкидка на следующий товар 30% при наличии этого чека")
                       os.system("pause")
                       break
                   elif answer == "N" or answer == "n":
                       print("Как жаль! Тогда удачи сдать свою работу")
                       break
                   else:
                       print("такого варианта нет, только y(yes), n(no)")
               else:
                   print("нет такого варинта ответа,напишите что-нибудь из списка")













