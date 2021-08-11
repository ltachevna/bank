dicte = {"g" : "п", "h" : "р", "b" : "и", "d" : "в", "t" : "е", "n" : "т"}
answer = input("напишите привет на английской раскладке:")
for key in enumerate(dicte.keys()):
    if key[1] != answer[key[0]]:
        print("неверно")
        break
else:
    print("красава")






