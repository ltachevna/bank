# house = [75, 25, 13]
# a = house[0] + house[1]
# print(a - house[2])

# school = [52, 23, 35, 16]
# a = school[1] + school[2]
# c = a - school[3]
# print(school[0] - c)


# a = []
# try:
#     print(a[1])
# except IndexError:
#     print("такого элемента нет")

#
# file = open("sdf.txt", 'r', encoding="utf-8")
# for line in file:
#     print(line)
# file.close()


def chek_int(line):
    variable = chek_int("хочу инт значение")
    while True:
        try:
            a = int(input("line"))
        except ValueError:
            print("введите норм значение")
        else:
            break
    return a
