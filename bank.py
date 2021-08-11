print("добро пожаловать в Альфа банк")
chek = input("напишите ваше ФИО:")
while True:
    number = input("напищите номер вашего телефона:")
    if number[:4] == "+375":
        if number[1:].isdigit():
            if len(number) == 13:
                print("ваш номер успешно зарегистрирован")
                break
    else:
        print("вы ввели неправильный номер")
while True:
    imeil = input("введите ваш имейл:")
    if "@" in imeil:
        if "." in imeil[imeil.index("@"):]:
            print("ваш имейл успешно зарегестрирован")
            break
    else:
        print("вы велли неправильный имейл")
karta = input("введите номер вашей карты:")
many = int(input("введите вашу сумму:"))
print("после успешной регестрации вы попали в меню:")
print("1.перевод на карту, 2.платёж, 3.заблокировать/разблокировать карту, 4.виписка из карты")
menu = input("что вы выбираете?:")
balance = 0
while True:
    if menu == "1":
        karta1 = input("введите номер карты:")
        term = input("введите срок годности:")
        if len(karta1) == 12:
            if "/" in term and len(term) == "4":
                if int(list[:term.index("/")]) >= 7 and int(list[term.index("/"):]) >= 21:
                    print("перевод успешно совершён")
        else:
            print("ваша карта недествительна либо неравильный ввод карты")
    elif menu == "2":
        payment = input("выберите платёж, который хотите совершить(ЕРИП, оплатить коммунальные услуги, оплата кредита и т.д:")
    elif menu == "3":
        state = input("какая именно услуга вас интересует?")
        if state == "заблокировать":
            pin = input("введите пин-код")
            for i in range(3):
                if len(pin) != 4:
                    print("ваша карта заблокирована, обратитесь в главный офис для её восстановления")
                else:
                    print("красавчик")
        elif state == "разблокировать":
            print("обратитесь в главный офис либо позвоните в коул центр")
    elif menu == "4":
        state1 = input("какая услуга вас интересует?:")
        suma = int(input("сумма перевода:"))
        if state1 == "баланс после перевода":
            balance = many - suma
            balance = int(balance)
            print(balance)
        elif state1 == "баланс после получения зп":
            balance1 = balance + suma
            print(balance1)
    elif menu == "0":
        print("вы завершили сеанс")
        break










