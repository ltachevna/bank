game = ["left", "right", "up", "down"]
x = 0
y = 0
while True:
    choice = input("куда пойдёт робот?")
    if choice == game[0]:
        x -= 1
    elif choice == game[1]:
        x += 1
    elif choice == game[2]:
        y += 1
    elif choice == game[3]:
        y -= 1
    else:
        break

if x >= 0:
    print("бот ущёл на", x,"вправо ")
elif x <= 0:
    print("робот ушёл на", x, "клнток влево")
elif y >= 0:
    print("робот ушёд на", y,"вверх")
elif y <= 0:
    print("робот ушёл на", y, "клеток вниз")

